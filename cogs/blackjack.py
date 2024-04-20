import discord
import random
from discord.ext import commands

class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='blackjack', aliases=['bj'], help='Starts a game of blackjack')
    async def blackjack(self, ctx):
        def create_deck():
            deck = []
            for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for rank in range(2, 11):
                    deck.append(str(rank) + ' of ' + suit)
                for face_card in ['Jack', 'Queen', 'King', 'Ace']:
                    deck.append(face_card + ' of ' + suit)
            random.shuffle(deck)
            return deck

        def calculate_hand_value(hand):
            value = 0
            num_aces = 0
            for card in hand:
                if card.startswith('Jack') or card.startswith('Queen') or card.startswith('King'):
                    value += 10
                elif card.startswith('Ace'):
                    num_aces += 1
                    value += 11
                else:
                    value += int(card.split()[0])
            while value > 21 and num_aces:
                value -= 10
                num_aces -= 1
            return value

        def check_win(player_value, dealer_value):
            # Adjust win probabilities
            win_probability = random.random()  # Generate a random number between 0 and 1

            # If the random number is less than 0.1 (10% chance), the player wins
            if win_probability < 0.3:
                return "Congratulations! You win!", 0x00ff00  # Green color

            # If the random number is between 0.1 and 0.8 (70% chance), the dealer wins
            elif 0.1 <= win_probability < 0.7:
                return "Dealer wins!", 0xff0000  # Red color

            # Otherwise, it's a tie
            else:
                return "It's a tie!", 0xffff00  # Yellow color

        # Initialize game
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value([dealer_hand[0]])  # Exclude one dealer card when calculating dealer's hand value

        # Create embed
        embed = discord.Embed(title="Blackjack Table", color=0x000000)

        dealer_hand_display = '\n'.join(['**'+dealer_hand[0]+'**', 'Hidden Card'])
        embed.add_field(name=f"Dealer Hand - ({dealer_value})", value=dealer_hand_display, inline=False)

        embed.add_field(name="-------------------------------------------------------------", value='\u200b', inline=False)

        player_hand_display = '\n'.join(player_hand)
        embed.add_field(name=f"{ctx.author.display_name}'s Hand - ({player_value})", value=player_hand_display, inline=False)

        message = await ctx.reply(embed=embed)

        # Add reactions
        await message.add_reaction('👍')  # Hit
        await message.add_reaction('👎')  # Stand

        # Player's turn
        while player_value < 21:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda r, u: u == ctx.author and r.message.id == message.id and str(r.emoji) in ['👍', '👎'])
            except:
                break  # Timeout or user's reaction not valid
            else:
                if str(reaction.emoji) == '👍':
                    player_hand.append(deck.pop())
                    player_value = calculate_hand_value(player_hand)
                    player_hand_display = '\n'.join(player_hand)
                    embed.set_field_at(2, name=f"{ctx.author.display_name}'s Hand - ({player_value})", value=player_hand_display)
                    await message.edit(embed=embed)
                elif str(reaction.emoji) == '👎':
                    break

            await message.remove_reaction(reaction, user)  # Remove the user's reaction after they make a choice

        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        dealer_hand_display = '\n'.join(dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        embed.set_field_at(0, name=f"Dealer Hand - ({dealer_value})", value=dealer_hand_display)
        await message.edit(embed=embed)

        # Determine the winner
        result, color = check_win(player_value, dealer_value)
        embed.add_field(name="Result", value=result, inline=False)
        embed.color = color  # Set the embed color based on the outcome
        await message.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(Blackjack(bot))
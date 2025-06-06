import random

# Configure multiple Reddit accounts
class Config:
    accounts = [
        {
            "client_id": "cBS1MRaVcqM72ChvqF6dEw",
            "client_secret": "7kWVJO7QvwpBoot3oVy8TWc3xqKFPA",
            "username": "Foreign_Rabbit8297",
            "password": "qwasopkl1290",
        },
        # Add more accounts as needed
        {
            "client_id": "AnotherClientID",
            "client_secret": "AnotherClientSecret",
            "username": "AnotherUsername",
            "password": "AnotherPassword",
        },
    ]

class Botconfig:
    proxies = [
        # Add more proxies as needed
    ]
    
    new_posts = False
    
    # Interval between posts or comments in minutes
    cooldown = 10 
    
    # Set to True if you need to setup webhook for logs
    webhook = ""
    
    discord_webhook = False
     
    # Select purpose of bot: 'ai', 'ad', or 'post'
    type = "ai"
    
    all_subreddits = True
    
    ads = [
        '''
        Advertisement 1: Type what u want to advertise here the exact same message will be commented on random posts!
        ''',
        '''
        Advertisement 2: Another ad message here!
        ''',
        '''
        Advertisement 3: Yet another ad message here!
        ''',
    ]
    
    # If set to False, will only post in the specific subreddits
    subreddits = [
        "test",
        "gachagaming",
        "TowerofGod",
    ]

    posts = [
        {"title": "Hey there, upvote for an upvote!", "body": "UPVOTE PLEASE"},
        {"title": "Upvote for upvote, part 2!", "body": "UPVOTE PLEASE"}
    ]
    
    log_file = "commented_posts.txt"

    @staticmethod
    def get_random_proxy():
        if Botconfig.proxies:
            return random.choice(Botconfig.proxies)
        return None

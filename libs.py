class Member: 
    def __init__(self, name):
        self.name = name
        self.is_subcribed = False
        self.subscription_duration = 0
    
    def unsubcribe(self):
        if(self.is_subcribed):
            self.is_subcribed = False
        else:
            print(f"Member {self.name} is already stop the subscription")
    
    def subcribe(self, subscription_duration):
        if(self.is_subcribed == False):
            self.is_subcribed = True
            self.subscription_duration = subscription_duration
        else:
            print(f"Member {self.name} is already subscription")
    

class StreamingPlatform:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.members = []
    
    def register_member(self, member: Member):
        self.members.append(member)

    def get_subcription_member(self):
        active_members = []
        for member in self.members:
            if member.is_subcribed:
                active_members.append(member)

        return active_members
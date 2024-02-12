class ConversationTracker:
    def __init__(self):
        self.conversations = []

    def add_conversation(self, conversation):
        self.conversations.append(conversation)

    def find_land_related_patterns(self):
        for conversation in self.conversations:
            land_mentions = []
            specifics_of_land = []
            for speaker, message in conversation:
                if "land" in message.lower():
                    land_mentions.append((speaker, message))
                elif "specifics" in message.lower():
                    specifics_of_land.append((speaker, message))
            if land_mentions and specifics_of_land:
                print("Potential pattern found:")
                print("Land mentions:", land_mentions)
                print("Specifics of land mentioned by:", specifics_of_land)

if __name__ == "__main__":
    tracker = ConversationTracker()

    conversation1 = [("Speaker A", "I have a piece of land."), ("Speaker B", "That's interesting.")]
    conversation2 = [("Speaker C", "Land is a valuable asset."), ("Speaker D", "I own 10 acres of land.")]
    conversation3 = [("Speaker E", "I want to invest in land."), ("Speaker F", "I know a great plot near the river.")]
    conversation4 = [("Speaker G", "Land prices are rising rapidly."), ("Speaker H", "I recently bought land in the countryside.")]

    tracker.add_conversation(conversation1)
    tracker.add_conversation(conversation2)
    tracker.add_conversation(conversation3)
    tracker.add_conversation(conversation4)

    tracker.find_land_related_patterns()

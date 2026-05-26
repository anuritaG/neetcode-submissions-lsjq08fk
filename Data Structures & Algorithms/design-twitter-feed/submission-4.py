class Twitter:

    # Maintain heap of time to tweets. While displaying feed, combine 10 feeds of
    # each follower and display
    def __init__(self):
        self.time = 0
        # user Id -> follower Id
        self.followers = collections.defaultdict(set)
        # each user: time -> tweets by them
        self.UserToTweetMap = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        tweets = self.UserToTweetMap[userId]
        self.UserToTweetMap[userId].append([self.time, tweetId])
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        feedHeap = []
        userIds = set(self.followers[userId])
        userIds.add(userId)
        
        res = []
        for uID in userIds:
            for tweetInfo in self.UserToTweetMap[uID][-10:]:
                time, tweetId = tweetInfo
                heapq.heappush(feedHeap, tweetInfo)

        while len(res) < 10 and feedHeap:
            item = heapq.heappop(feedHeap)
            res.append(item[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # print("before", self.followers, " ", followerId, " ",followeeId )
        self.followers[followerId].add(followeeId)
        # print("after", self.followers)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

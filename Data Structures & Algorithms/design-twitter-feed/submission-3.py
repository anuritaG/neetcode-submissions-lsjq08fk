class Twitter:

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
        # print("followers,", self.followers)
        # print("getNews", userId)
        userIds = set(self.followers[userId])
        # print("followers", userIds)
        userIds.add(userId)
        
        # print("followers", userIds)
        res = []
        print(self.UserToTweetMap)
        for uID in userIds:
            # print("uID", uID, " ", self.UserToTweetMap[uID])
            for tweetInfo in self.UserToTweetMap[uID][-10:]:
                # print("te",tweetInfo)
                time, tweetId = tweetInfo
                heapq.heappush(feedHeap, tweetInfo)
                # if len(feedHeap) > 10:
                #     tweet = heapq.heappop(feedHeap)
                #     res.append(tweet[1])
        
        
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
        

print ()

import math
from operator import itemgetter

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Pearson Correlation between two vectors
    def pearson(self):
        
        sum_p = 0
        sum_q = 0
        sum_pq = 0
        square_sum_p = 0
        square_sum_q = 0

        # Step 1.1
        # set n to the number of common keys
        n = len(set(self.ratings1.keys()) & set(self.ratings2.keys()))
            
        # Step 1.2
        # error check for n==0 condition, and return -2 if n==0
        if n == 0:
            return -2

        # Step 1.3
        # use a SINGLE for loop to calculate the partial sums in the computationally efficient form of the pearson correlation  
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            sum_p += p
            sum_q += q
            sum_pq += p * q
            square_sum_p += pow(p, 2)
            square_sum_q += pow(q, 2)

        # Step 1.4
        # calculate the numerator term for pearson correlation using relevant partial sums
        numerator = sum_pq - ((sum_p * sum_q)/n)
        
        # Step 1.5
        # calculate the denominator term for pearson correlation using relevant partial sums
        denominator = ((square_sum_p - pow(sum_p, 2)/n) * (square_sum_q - pow(sum_q, 2)/n)) ** 0.5
        
        # Step 1.6
        # error check for denominator==0 condition and return -2 if denominator==0
        if denominator == 0: 
            return -2

        # Step 1.7
        # calculate the pearson correlation using the numerator and denominator and return the pearson correlation
        result = numerator/denominator
        return result


# user ratings - this is the same data as we used in the User Recommendation Lecture
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

# for whom are we making recommendations?
userX = "Veronica"
userXRatings = songData[userX]
from operator import itemgetter

# Step 2.1
# find the similarity measure (pearson correlation) between userX's ratings, and each of the other user's ratings.
userSimilarities = []
for userY, userYRatings in songData.items():
    if userY != userX:
        s = similarity(songData[userX], songData[userY])
        pearsonXY = s.pearson()
        lst = (userY, pearsonXY)
        userSimilarities.append(lst)

# Step 2.2
# sort the list of tuples by highest similarity to lowest similarity and assign the sorted list to a variable called sortedUserSimilarities.
sortedUserSimilarities = sorted(userSimilarities, key=itemgetter(1), reverse=True)

# Step 2.3
# userX's NN is the user at the 0th position of the sorted list and assign the NN to a variable called userXNN.
userXNN = sortedUserSimilarities[0][0]

# Step 2.4
# recos for userX should include albums rated by userXNN, not already rated by userX.
# assign the list of (album, rating) tuples to a variable called userXRecos.
userXRecos = []
for x in songData[userXNN]:
    if x not in songData[userX]:
        userXRecos.append((x, songData[userXNN][x]))

print(userXRecos)

# Step 2.5
# sort list of tuples by highest rating to lowest rating and assign sorted list to a variable userXSortedRecos.
userXSortedRecos = []
userXSortedRecos = sorted(userXRecos, key=itemgetter(1))

print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)


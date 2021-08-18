from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the sprint index.")

@csrf_exempt
def selectStories(request):
    if request.method == 'GET':
        return HttpResponse("select stories route.")
    elif request.method == 'POST':
        data = request.POST
        received_json_data=json.loads(request.body)
        stories = received_json_data["stories"]
        sprint_point = received_json_data["sprint_point"]
        #print(stories, sprint_point)
        #returnknapSack(W, wt, val, n)
        wt = []
        val = []
        item = []
        for i in stories:
            wt.append(i["story_point"])
            val.append(i["story_point"])
            item.append(i["story_name"])
        n = len(stories)
        res_item,res_item_index = returnknapSack(sprint_point, wt, val, n)
        #print(res_item, res_item_index)
        result = []
        sum = 0
        for i in reversed(range(len(res_item_index))):
            index = res_item_index[i]
            result.append(stories[index])
            sum += res_item[i]
        #print(result, sum)
        return HttpResponse(json.dumps({"result": result, "sum": sum}), content_type='application/json')

def returnknapSack(W, wt, val, n):
    res_item = []
    res_item_index = []
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    #print(res)
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            res_item.append(wt[i - 1])
            res_item_index.append(i-1)
            #print(wt[i - 1], i-1)
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return (res_item,res_item_index)
 
# Driver code
# val = [ 1, 1, 1, 1, 1, 1, 1, 1 ]
# wt = [ 2, 3, 5, 8, 4, 6, 2, 1 ]
# W = 14
#val = [ 60, 100, 120 ]
#wt = [ 10, 20, 30 ]
#W = 50
# n = len(val)
     
# print(printknapSack(W, wt, val, n))

# Create your views here.

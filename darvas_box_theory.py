#DARVAS BOX THEORY SCRIPT

########## Functions to be implemented ##########

## DetermineBox() returns two vals, upper and lower
def DetermineBox(str stock):
    ## Use name of stock to find high/low
    ## Are boxes defined by average low/high or lowest/highest?


    ## Return the upper and lower bounds
    return upper, lower
    
## 2D array Boxes[[GGL][143, 151] ] should hold all of the stocks, along with their current high/low box

## FindValue() finds the current value of a stock by searching web (or app)
def FindValue(str stock):
    int value
    
    
    return value


## Find the volume of stocks traded
def FindVolume(str stock):
    int volume

    return volume

## MakeDecision() compares the current stock value with the box and says whether to buy or sell
def MakeDecision(upper, lower, current_val  ):
    

## main() loops every certain time period (e.g. ever 15 mins) doing the following.
## DetermineBox() or GetBox()

def main():
    ## While the script is running
    while (true):
        ## Determine boxes
        for stock in stock_list:
            # Not correct syntax, just example of logic.
            box = DetermineBox(stock)
            full_box = [[stock][box.upper, box.lower]]
            Boxes.add[full_box]
        # Find current vals
        for stock in stock_list:
            current_val = FindValue(stock)
            # list of current value, should have same index as stock in boxes array
            current_vals.add(current_val)

        for i in stock_list:
            decision = MakeDecision(boxes[i], current_vals[i])
            
        
        


def sum67(nums):
  
  sum = 0
  counting = True
  
  for i in nums:
    
    if i == 6 and counting:
      counting = False
        
    elif i == 7 and not counting:
      counting = True

    print(i, counting, sum)  
    if counting:
      sum = sum + i
    
  return sum

print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))

z : 1 True 0
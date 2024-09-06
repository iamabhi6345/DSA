def max_networks(n, speed, minComps, speedThreshold):
    count = 0
    i = 0
    
    while i < n:
        total_speed = 0
        num_computers = 0
        
        # Form a network starting from computer i
        while i < n and num_computers < minComps:
            total_speed += speed[i]
            num_computers += 1
            i += 1
        
        # Check if the network meets the speed threshold
        while i < n and total_speed < speedThreshold:
            total_speed += speed[i]
            num_computers += 1
            i += 1
            
        # If we have at least minComps and total_speed >= speedThreshold, count this network
        if num_computers >= minComps and total_speed >= speedThreshold:
            count += 1
    
    return count

# Example usage
n = 7
speed = [5, 7, 9, 12, 10, 13,8]
minComps = 2
speedThreshold = 15

print(max_networks(n, speed, minComps, speedThreshold))  # Output: 2

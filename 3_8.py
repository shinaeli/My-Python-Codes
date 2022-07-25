places_to_visit = ['United States of America', 'France', 'Australia', 'Dubai', 'United Kingdom']

print(places_to_visit)

sorted_places_to_visit = sorted(places_to_visit)
print(sorted_places_to_visit) #['Australia', 'Dubai', 'France', 'United Kingdom', 'United States of America']
print(places_to_visit) #['United States of America', 'France', 'Australia', 'Dubai', 'United Kingdom']

reverse_sorted_places_to_visit = sorted(places_to_visit, reverse=True)
print(reverse_sorted_places_to_visit) #['United States of America', 'United Kingdom', 'France', 'Dubai', 'Australia']
print(places_to_visit) #['United States of America', 'France', 'Australia', 'Dubai', 'United Kingdom']

places_to_visit.reverse()
print(places_to_visit) #['United Kingdom', 'Dubai', 'Australia', 'France', 'United States of America']

places_to_visit.reverse()
print(places_to_visit) #['United States of America', 'France', 'Australia', 'Dubai', 'United Kingdom']

places_to_visit.sort()
print(places_to_visit) #['Australia', 'Dubai', 'France', 'United Kingdom', 'United States of America']

places_to_visit.sort(reverse=True)
print(places_to_visit) #['United States of America', 'United Kingdom', 'France', 'Dubai', 'Australia']
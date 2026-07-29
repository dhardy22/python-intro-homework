languages_a = ["JavaScript", "Java","C++", "Swift", "HTML", "Rust", "TypeScript", "Perl", "Java"]
languages_b = ["SQL", "Python","C++", "R", "SQL", "C", "Java","MATLAB", "Swift", "COBOL"]


languages_a_set = set(languages_a)
languages_b_set = set(languages_b)

print(languages_a_set.union(languages_b_set))  #Output: {'Java', 'Swift', 'TypeScript', 'JavaScript', 'C', 'C++', 'SQL', 'R', 'Python', 'HTML', 'MATLAB', 'Perl', 'COBOL', 'Rust'}
# print(len(languages_a_set.union(languages_b_set)))

#Prints the values that both list share. Order does not matter
print(languages_b_set.intersection(languages_a_set))
# print(len(languages_b_set.intersection(languages_a_set)))

#prints unique values from the first set with the .difference argument applied. Order matters
print(languages_a_set.difference(languages_b_set))
# print(len(languages_a_set.difference(languages_b_set)))





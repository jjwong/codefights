1. s = 'abacaba'
2. s = "abacaba"
3. s = ''abacaba''
4. s = ""abacaba""
5. s = '''abacaba'''
6. s = """abacaba"""

# Since there are no comments available for this problem on codefights, I can explain here why option 3 and 4
# are considered incorrect.
#
# Option 1 and 2 denote a regular string
# Option 5 and 6 denote docstrings
# Option 3 and 4 denote an empty string('') and does not append abacaba
#   If you wanted to append the string you would instead do
#       '' + 'abacaba' + ''
#       or just 'abacaba' since empty strings don't mean a whole lot here.
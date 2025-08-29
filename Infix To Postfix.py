oper=set(['+','-','*','/','(',')','^'])
pri={'+':1,'-':1,'*':2,'/':2,'^':3}
def infixtopostfix(expression):
    stack=[]
    output=''
    for ch in expression:
        if ch not in oper:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='('and pri [ch]<=pri[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
expression=input("enter infix expression ")
print("infix expression: ",expression)
print("postfix expression: ",infixtopostfix(expression))

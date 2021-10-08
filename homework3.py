# task1.
name = input('enter your name:')
if name == 'Danya':
    print('its my name too')
else:
 print('its differs from mine')

# task2
operation = input('''
select ur operation:
*
/
+
-
''')

x = int(input('enter your first number:'))
y = int(input('enter your second number:'))


if operation == '*':
    print('your result',x*y)
elif operation == '/':
    print('your result',x/y)
elif operation == '+':
    print('your result',x+y)
elif operation == '-':
        print('your result',x-y)
else:
    print('incorrect operation,have a nice day')



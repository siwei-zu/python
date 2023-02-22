#转义字符

print("hello\nworld")#换行
print("hello\bworld")#退格
print("hello\tworld")#制表符，注意：如果制表符前面刚好够一个制表符，那么就往后加四个空格，如果不够，追加剩余的空格

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上个‘r’或‘R’
print(r"hello\nworld")
print(R"hello\tworld")
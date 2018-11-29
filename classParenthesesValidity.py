class Text_Parentheses:
    def __init__(self, text):
        self.text = text

        open_p = ['(', '[', '{']
        close_p = [')', ']', '}']
        dic = dict(zip(open_p, close_p))
        stack = ''

        for char in text:
            if char in open_p:  # adciona no stack
                stack += char
            elif char in close_p:  # checa o stack
                if (len(stack) == 0) or (dic[stack[-1]] != char):  # se nao tiver nenhum parenteses aberto ou nao se o ultimo aberto nao bate com o que esta fechando
                    self.validity = False
                    break
                stack = stack[:-1]  # se estiver tudo certo, retiro o ultimo parentese aberto do stack
        else:
            if len(stack) == 0:  # se nao tiver nenhum aberto precisando fechar
                self.validity = True
            else:
                self.validity = False


string = Text_Parentheses('esse e um teste {}}')

print(string.text, string.validity)

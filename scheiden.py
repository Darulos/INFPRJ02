i = 0
j = len(self.converter)
x = 0
# Show the questions
if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5))
screen.blit(question_block, question_rect)

if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+50))
screen.blit(question_block, question_rect)

if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+100))
screen.blit(question_block, question_rect)

if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+150))
screen.blit(question_block, question_rect)

if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+200))
screen.blit(question_block, question_rect)

if i+30 < j and self.converter[i+30] == " ":
    converteroutput = self.converter[i:i+30]
    i += 30
else:
    x = i
    for i in range(x + 30):
        if (x + 30)>= j:
            converteroutput = self.converter[x:j]
            i += 1000
            break
        elif self.converter[(x + 30) - i] == " ":
            converteroutput = self.converter[x:(x + 30) - i]
            i = x+30-i
            break
question_block = self.font.render(converteroutput, 1, (0, 255, 255))
question_rect = question_block.get_rect(center=(self.screenwidth/6, self.screenheight/5+250))
screen.blit(question_block, question_rect)

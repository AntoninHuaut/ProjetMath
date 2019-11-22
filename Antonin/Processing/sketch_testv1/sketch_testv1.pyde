global count, msgList
count = 1

msgList = {1: "Situation de départ", 2: "Génération des pairs de clés pour Alice", 3: "Génération des pairs de clés pour Bob"}

def setup():
    size(700, 700)
    textAlign(CENTER);
    global alice, bob, etape
    
    alice = Bloc(100, 100, 100, 0)
    aliceTxt = Txt("Alice", 26)
    aliceTxt.updatePosBloc(alice)
    alice.setTxt(aliceTxt)
    
    bob = Bloc(600, 400, 100, -1)
    bobTxt = Txt("Bob", 26)
    bobTxt.updatePosBloc(bob)
    bob.setTxt(bobTxt)
    
    etape = Txt("Etape", 32)
    etape.updatePos(width/2, height - height/5)
    etape.setCouleur(255, 204, 0)
 
def draw():
    #frameRate(0.3)
    frameRate(0.5)
    background(128)
    global count
    
    alice.show()
    bob.show()
    
    newTexte = "Etape " + str(count)
    
    if count in msgList:
        newTexte += "\n" + msgList.get(count)
    
    etape.setTexte(newTexte)
    etape.show()
    
    count += 1
    
class Bloc:
  def __init__(self, x, y, taille, speed):
    self.x = x
    self.y = y
    self.speed = speed
    self.taille = taille

  def reverse(self):
    self.speed = -self.speed

  def update(self):
    self.x += self.speed;
    
  def setTxt(self, txt):
      self.txt = txt
    
  def getTxt(self):
      return self.txt

  def show(self):
    rectMode(CENTER)
    fill(255, 204, 0)
    noStroke()
    rect(self.x, self.y, self.taille, self.taille);
    self.txt.show()
    
class Txt:
    def __init__(self, texte, texteSize):
        self.texteSize = texteSize
        self.taille = -1
        self.setTexte(texte)
        self.setCouleur(0, 0, 0)
        
    def setTexte(self, texte):
        self.texte = texte.decode('utf-8')
        
    def setCouleur(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def updatePos(self, x, y):
        self.x = x
        self.y = y
        
    def updatePosBloc(self, bloc):
        self.x = bloc.x
        self.y = bloc.y + 10
        self.taille = bloc.taille
        
    def show(self):
        fill(self.red, self.green, self.blue);
        textSize(self.texteSize);
        if self.taille == -1:
            text(self.texte, self.x, self.y + 10); 
        else:
            text(self.texte, self.x, self.y + 10, self.taille, self.taille);

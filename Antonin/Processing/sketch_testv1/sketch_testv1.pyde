global tick, nbEtape, msgEtape, imgPublic, imgPrivee, imgBob, imgAlice
tick, nbEtape = 1, 1
msgEtape = {1: "Situation de départ : Alice & Bob", 2: "Alice : génération de la paire de clés", 3: "Bob : génération de la paire de clés"}

def setup():
    frameRate(30)
    size(850, 850)
    textAlign(CENTER);
    global alice, bob, etape, imgPublic, imgPrivee, imgAlice, imgBob
    
    imgPublic = loadImage("clePublic.png")
    imgPrivee = loadImage("clePrivee.png")
    imgAlice = loadImage("bFemme.png")
    imgBob = loadImage("bHomme.png")
    
    alice = Personne(150, 150, 200, "top", "Alice")
    bob = Personne(width - 150, height - 350, 200, "bot", "Bob")
    
    etape = Txt("Etape", 32)
    etape.updatePos(width/2, height - 100)
    etape.setCouleur(255, 204, 0)
 
def draw():
    background(128)
    global tick, nbEtape
    
    alice.show()
    bob.show()
    
    newTexte = "Etape " + str(nbEtape) + "\n" + msgEtape.get(nbEtape)
    
    etape.setTexte(newTexte)
    etape.show()
    
    executeAction()
    tick += 1

def executeAction():
    if nbEtape >= 2:
        alice.showCle()
    if nbEtape >= 3:
        bob.showCle()

def keyReleased():
    """Permet de changer l'étape actuel via les touches flèches (gauche/droite) """
    global nbEtape
    
    if keyCode == 37:
        if nbEtape-1 in msgEtape:
            nbEtape -= 1
    elif keyCode == 39:
        if nbEtape+1 in msgEtape:
            nbEtape += 1
    
class Personne:
  def __init__(self, x, y, taille, pos, nom):
    self.x = x
    self.y = y
    self.taille = taille
    self.txt = Txt(nom, 26)
    self.txt.updatePosBloc(self)

    if nom == "Alice":
        self.imgPerso = ImagePerso(imgAlice, self.x, self.y)
    else:
        self.imgPerso = ImagePerso(imgBob, self.x, self.y)
    
    cle1 = Cle(self.x - self.taille/3, self.y - self.taille/3)
    cle2 = Cle(self.x - self.taille/3, self.y - self.taille/3)
    cle1.addPos(self.taille/1.75, self.taille/1.75)
    cle2.addPos(-self.taille*0.125, -self.taille*0.125)
        
    if pos == "top":
        self.publicCle = cle1
        self.priveCle = cle2
    else:
        self.publicCle = cle2
        self.priveCle = cle1
        
    self.publicCle.setNom("PUBLIC")
    self.priveCle.setNom("PRIVEE")

  def showCle(self):
      self.publicCle.show()
      self.priveCle.show()

  def update(self):
      self.x += self.speed;
    
  def getTxt(self):
      return self.txt

  def show(self):
      rectMode(CENTER)
      fill(255, 204, 0)
      noStroke()
      rect(self.x, self.y, self.taille, self.taille);
      
      self.imgPerso.show()
      self.txt.show()

class ImagePerso:
    def __init__(self, img, x, y):
        self.img = img
        self.height = 128
        self.width = self.height * 359/674
        self.x = x - self.width/2
        self.y = y - self.height/3
        
    def show(self):
        image(self.img, self.x, self.y, self.width, self.height)

class Cle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.circTaille = 50
        self.recTailleX = 30
        self.recTailleY = 10
        
    def setNom(self, nom):
        self.nom = nom
        
    def addPos(self, x, y):
        self.x += x
        self.y += y
        
    def show(self):
        if self.nom == "PUBLIC":
            image(imgPublic,  self.x, self.y, 48, 48)
        elif self.nom == "PRIVEE":
            image(imgPrivee,  self.x, self.y, 48, 48)

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
        self.y = bloc.y - bloc.taille/3.5
        self.taille = bloc.taille
        
    def show(self):
        fill(self.red, self.green, self.blue);
        textSize(self.texteSize);
        if self.taille == -1:
            text(self.texte, self.x, self.y + 10); 
        else:
            text(self.texte, self.x, self.y + self.taille/3, self.taille, self.taille);

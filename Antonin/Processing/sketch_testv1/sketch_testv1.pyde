global speedAnim, framerate, nbEtape, msgEtape, imgPublicAlice, imgPublicBob, imgPriveeAlice, imgPriveeBob, imgBob, imgAlice, inAnimation

# CONFIGURATION
framerate, speedAnim = 60, 2.5
# -------------

nbEtape, inAnimation = 0, 0
msgEtape = ["Situation de départ : Alice et Bob\nveulent s'envoyer un message", "Ils ne veulent pas que leurs messages\npuissent être lus par d'autres personnes", "Alice : génération de la paire de clés", "Bob : génération de la paire de clés",
            "Bob récupère la clé publique d'Alice"]

def setup():
    frameRate(framerate)
    size(850, 850)
    textAlign(CENTER);
    global alice, bob, etape, imgPublicAlice, imgPublicBob, imgPriveeAlice, imgPriveeBob, imgAlice, imgBob, nbEtape
    
    imgPublicAlice = loadImage("clePublicAlice.png")
    imgPublicBob = loadImage("clePublicBob.png")
    imgPriveeAlice = loadImage("clePriveeAlice.png")
    imgPriveeBob = loadImage("clePriveeBob.png")
    imgAlice = loadImage("bFemme.png")
    imgBob = loadImage("bHomme.png")
    
    alice = Personne(150, 150, 200, "top", "Alice")
    bob = Personne(width - 150, height - 350, 200, "bot", "Bob")
    
    etape = Txt("Etape", 32)
    etape.updatePos(width/2, height - 125)
    etape.setCouleur(255, 204, 0)
 
def draw():
    background(128)
    global nbEtape
    
    alice.show()
    bob.show()
    
    newTexte = "Etape " + str(nbEtape+1) + "\n" + msgEtape[nbEtape]
    
    etape.setTexte(newTexte)
    etape.show()
    
    executeAction()

global cleAnim

def executeAction():
    global inAnimation, cleAnim
    if nbEtape >= 2:
        alice.showCle()
    if nbEtape >= 3:
        bob.showCle()
    if nbEtape == 4:
        if inAnimation == 0:
            inAnimation = 1
            cleAnim = alice.getCles()[0]
        elif cleAnim.y >= bob.publicCle.y:
            resetAnim()
        else:
            cleAnim.show()
            cleAnim.addPos(0.975 * speedAnim, 0.5 * speedAnim)
            
def resetAnim():
    global inAnimation
    inAnimation = 0

def keyReleased():
    """Permet de changer l'étape actuel via les touches flèches (gauche/droite) """
    global nbEtape
    
    if not (keyCode == 37 or keyCode == 39): return
        
    resetAnim()
    
    if keyCode == 37:
        if nbEtape > 0:
            nbEtape -= 1
    elif keyCode == 39:
        if nbEtape+1 < len(msgEtape):
            nbEtape += 1
    
class Personne:
  def __init__(self, x, y, taille, pos, nom):
    self.x = x
    self.y = y
    self.taille = taille
    self.txt = Txt(nom, 26)
    self.txt.updatePosBloc(self)
    self.pos = pos
    self.nom = nom

    if nom == "Alice":
        self.imgPerso = ImagePerso(imgAlice, self.x, self.y)
    else:
        self.imgPerso = ImagePerso(imgBob, self.x, self.y)
    
    cles = self.getCles()
    self.publicCle = cles[0]
    self.priveCle = cles[1]
    
  def genCle(self):
      return Cle(self.x - self.taille/3, self.y - self.taille/3, self)
  
  def genClePos(self):
      cle1 = self.genCle()
      cle2 = self.genCle()
      cle1.addPos(self.taille/1.75, self.taille/1.75)
      cle2.addPos(-self.taille*0.125, -self.taille*0.125)
      return [cle1, cle2]
  
  def getCles(self): # Arg[0] = public arg[1] = privé
      cles = self.genClePos()
      if self.pos == "top":
          cles = [cles[0], cles[1]]
      else:
          cles = [cles[1], cles[0]]
      cles[0].setNom("PUBLIC")
      cles[1].setNom("PRIVEE")
      return cles

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
    def __init__(self, x, y, personne):
        self.x = x
        self.y = y
        self.personne = personne
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
            if self.personne.nom == "Alice":
                image(imgPublicAlice,  self.x, self.y, 48, 48)
            else:
                image(imgPublicBob,  self.x, self.y, 48, 48)
        elif self.nom == "PRIVEE":
            if self.personne.nom == "Alice":
                image(imgPriveeAlice,  self.x, self.y, 48, 48)
            else:
                image(imgPriveeBob,  self.x, self.y, 48, 48)

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

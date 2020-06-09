from abc import ABC, abstractmethod

class Animal(ABC):
    "It Represents Animalia Kingdom"
    __count = 0
    vertebrates = ("Mammal", "Bird", "Reptile", "Fish", "Amphibian")

    @classmethod
    def getCount(cls):
        return cls.__count

    def __init__(self):
        super().__init__()
        Animal.__count += 1
    
    def __str__(self):
        return "Animal"

    def isVertebrate(self):
        if(self() in self.vertebrates):
            return True
        return False

    def hasBeak(self):
        return (self() == "Bird")
        
    def hasScales(self):
        return (self() in self.vertebrates[2:])
        
    def isColdBlooded(self):
        return (not self.isWarmBlooded())

    @abstractmethod
    def isWarmBlooded(self):
        pass

    @abstractmethod
    def isAquatic(self):
        pass

    @abstractmethod
    def isFlyable(self):
        pass

    @abstractmethod
    def __call__(self):
        pass

    @classmethod
    @abstractmethod
    def getBinomialNomenclature(cls):
        pass

class Fish(Animal, ABC):
    "It Represents Pisches evolved from Animals"
    __count = 0

    @classmethod
    def getCount(cls):
        return cls.__count

    def __init__(self):
        super().__init__()
        Fish.__count += 1

    def __str__(self):
        return "Fish"

    def __call__(self):
        return "Fish"

    def hasFins(self):
        return not (self._fins == 0)

    def isAquatic(self):
        return True

    def hasGills(self):
        return not (self._gills == 0)

    @classmethod
    @abstractmethod
    def getBinomialNomenclature(cls):
        pass

    @abstractmethod
    def setFins(self):
        pass

    @abstractmethod
    def getFins(self):
        pass

    def hasTentacles(self):
        return not (self._tentacles == 0)

    @abstractmethod
    def isEatable(self):
        pass

    @abstractmethod
    def setTentacles(self):
        pass

    @abstractmethod
    def getTentacles(self):
        pass

    @abstractmethod
    def isFriend(self):
        pass

    def isWarmBlooded(self):
        return False

    def isFlyable(self):
        return False

class SeerFish(Fish):
    "It is a popular Fish in Arabian Sea."
    __count = 0
    __binomialNomenclature = "Scomberomorus guttatus"

    @classmethod
    def getBinomialNomenclature(cls):
        return cls.__binomialNomenclature

    def setHeartChambers(self, heartChambers = 2):
        self._heartChambers = heartChambers
        return True

    def getHeartChambers(self):
        return self._heartChambers

    def __init__(self, name = "Anonymous", fins = 2, gills = 2, tentacles = 0, localNames = [], heartChambers = 2):
        super().__init__()
        self.setName(name)
        self.setLocalNames(localNames)
        self.setFins(fins)
        self.setGills(gills)
        self.setTentacles(tentacles)
        SeerFish.__count += 1
        self._heartChambers = heartChambers

    def getName(Self):
        return self._name
        
    def setName(self, name = "Anonymous"):
        self._name = name
        return True

    def setLocalNames(self, localNames = []):
        self._localNames = localNames
        return True

    def getLocalNames(self):
        return self._localNames

    def setFins(self, fins = 2):
        self._fins = fins
        return True

    def setGills(self, gills = 2):
        self._gills = gills
        return self._gills

    def getFins(self):
        return self._fins

    def isEatable(self):
        return True

    def setTentacles(self, tentacles = 0):
        self._tentacles = tentacles
        return True

    def getTentacles(self):
        return self._tentacles

    def isFriend(self):
        return True

class Octopus(Fish):
    "It is the most venomous aquatic creature."
    __count = 0
    __binomialNomenclature = "Octopus vulgaris"

    @classmethod
    def getBinomialNomenclature(cls):
        return cls.__binomialNomenclature

    def __init__(self, fins = 0, gills = 2, tentacles = 8, numberOfHearts = 3, heartChambers = 2, localNames = []):
        super().__init__()
        self.setLocalNames(localNames)
        self.setFins(fins)
        self.setGills(gills)
        self.setTentacles(tentacles)
        self.setHearts(numberOfHearts)
        Octopus.__count += 1
        self.setHeartChambers(heartChambers)

    def setHeartChambers(self, heartChambers = 2):
        self._heartChambers = heartChambers
        return True

    def getHeartChambers(self):
        return self._heartChambers

    def getNumberOfHearts(self):
        return self._numberOfHearts

    def setNumberOfHearts(self, numberOfHearts):
        self._numberOfHearts = numberOfHearts
        return True

    def setLocalNames(self, localNames = []):
        self._localNames = localNames
        return True

    def getLocalNames(self):
        return self._localNames

    def setFins(self, fins = 0):
        self._fins = fins
        return True

    def setGills(self, gills = 2):
        self._gills = gills
        return self._gills

    def getFins(self):
        return self._fins

    def isEatable(self):
        return True

    def setTentacles(self, tentacles = 8):
        self._tentacles = tentacles
        return True

    def getTentacles(self):
        return self._tentacles

    def isFriend(self):
        return "Rarely True"

class Mammal(Animal, ABC):
    "It Represents Mammalians evolved from Animals"
    __count = 0

    @classmethod
    def getCount(cls):
        return cls.__count
    
    def __init__(self):
        super().__init__()
        Mammal.__count += 1

    def __str__(self):
        return "Mammal"

    def __call__(self):
        return "Mammal"

    def isFlyable(self):
        return False

    def isWarmBlooded(self):
        return True

    def hasHair(self):
        return (str(self) == "Human")
    
    def hasFur(self):
        return not (str(self) == "Human")

    def hasHands(self):
        return not (self._hands == 0)

    def hasLegs(self):
        return not (self._legs == 0)

    def hasFins(self):
        return not (self._fins == 0)

    @abstractmethod
    def isAquatic(self):
        pass

    @abstractmethod
    def setLegs(self):
        pass

    @abstractmethod
    def setHands(self):
        pass

    @abstractmethod
    def setFins(self):
        pass
    
    @abstractmethod
    def getFins(self):
        pass

    @abstractmethod
    def getLegs(self):
        pass

    @abstractmethod
    def getHands(self):
        pass

    @classmethod
    @abstractmethod
    def getBinomialNomenclature(cls):
        pass

class Human(Mammal):
    "It is the most thinking-wise evolved animal."
    __count = 0
    __binomialNomenclature = "Homo Sapien"

    @classmethod
    def getCount(cls):
        return cls.__count

    @classmethod
    def getBinomialNomenclature(self):
        return self.__binomialNomenclature

    def __init__(self, name = "Anonymous", age = 0, hands = 2, legs = 2, fins = 0, heartChambers = 4):
        super().__init__()
        self.setName(name)
        self.setAge(age)
        self.setHands(hands)
        self.setLegs(legs)
        self.setFins(fins)
        self.setHeartChambers(heartChambers)
        Human.__count += 1

    def __str__(self):
        return "Human"

    def setName(self, name = "Anonymous"):
        self._name = name
        
    def getName(self):
        return self._name

    def setLegs(self, legs = 2):
        self._legs = legs

    def setHands(self, hands = 2):
        self._hands = hands

    def setFins(self, fins = 0):
        self._fins = fins

    def getFins(self):
        return self._fins

    def getLegs(self):
        return self._legs

    def getHands(self):
        return self._hands
    
    def setHeartChambers(self, heartChambers = 4):
        self._heartChambers = heartChambers
        return True
    
    def getHeartChambers(self):
        return self._heartChambers

    def setAge(self, age):
        self._age = age
        return True

    def getAge(self):
        return self._age

class Dolphin(Mammal):
    "It is one of the Human's oceanic friend."
    __count = 0
    __binomialNomenclature = "Delphinus capensis"

    @classmethod
    def getBinomialNomenclature(cls):
        return cls.__binomialNomenclature

    def setHeartChambers(self, heartChambers = 4):
        self._heartChambers = heartChambers
        return True

    def getHeartChambers(self):
        return self._heartChambers

    def __init__(self, name = "Anonymous", fins = 2, hands = 0, legs = 0, localNames = [], heartChambers = 4):
        super().__init__()
        self.setName(name)
        self.setLocalNames(localNames)
        self.setFins(fins)
        self.setHands(hands)
        self.setLegs(legs)
        Dolphin.__count += 1
        self.setHeartChambers(heartChambers)

    def getName(Self):
        return self._name
        
    def setName(self, name = "Anonymous"):
        self._name = name
        return True

    def setLocalNames(self, localNames = []):
        self._localNames = localNames
        return True

    def getLocalNames(self):
        return self._localNames

    def isEatable(self):
        return "Rarely True"

    def isFriend(self):
        return True

    def __str__(self):
        return "Dolphin"

    def isAquatic(self):
        return True

    def setLegs(self, legs = 0):
        self._legs = legs
        return True

    def setHands(self, hands = 0):
        self._hands = hands
        return True

    def setFins(self, fins = 2):
        self._fins = fins
        return True
    
    def getFins(self):
        return self._fins

    def getLegs(self):
        return self._legs

    def getHands(self):
        return self._hands

class Bird(Animal, ABC):
    "It Represents Aves evolved from Animals"
    __count = 0

    @classmethod
    def getCount(cls):
        return cls.__count

    def __init__(self):
        super().__init__()
        Bird.__count += 1

    def __call__(self):
        return "Bird"
            
    def __str__(self):
        return "Bird"

    def isWarmBlooded(self):
        return True

    @abstractmethod
    def isAquatic(self):
        pass

    @abstractmethod
    def isFlyable(self):
        pass

    @classmethod
    @abstractmethod
    def getBinomialNomenclature(cls):
        pass

class Duck(Bird):
    "It is the most beautiful bird living over Waters."
    __count = 0
    __binomialNomenclature = "Anas Platyrhynchos"

    @classmethod
    def getCount(cls):
        return cls.__count

    @classmethod
    def getBinomialNomenclature(cls):
        return cls.__binomialNomenclature

    def setHeartChambers(self, heartChambers = 4):
        self._heartChambers = heartChambers
        return True

    def getHeartChambers(self):
        return self._heartChambers

    def __init__(self, name = "Anonymous", furcolor = "White", commonCall = "Quack", localNames = [], heartChambers = 4):
        super().__init__()
        self.setName(name)
        self.setLocalNames(localNames)
        self.setFurcolor(furcolor)
        self.setCommonCall(commonCall)
        Duck.__count += 1
        self.setHeartChambers(heartChambers)

    def setCommonCall(self, commonCall = "Quack"):
        self._commonCall = commonCall
        return True

    def getCommonCall(self):
        return self._commonCall

    def setFurcolor(self, furcolor = "White"):
        self._furcolor = furcolor
        return True

    def getFurcolor(self):
        return self._furcolor

    def getName(self):
        return self._name
        
    def setName(self, name = "Anonymous"):
        self._name = name
        return True

    def setLocalNames(self, localNames = []):
        self._localNames = localNames
        return True

    def getLocalNames(self):
        return self._localNames

    def isEatable(self):
        return True

    def isFriend(self):
        return True
    
    def isAquatic(self):
        return True

    def isFlyable(self):
        return False

    def __str__(self):
        return "Duck"

class Crow(Bird):
    "It is the most annoying creature and most common everywhere."
    __count = 0
    __binomialNomenclature = "Corvus brachyrhynchos"

    @classmethod
    def getCount(cls):
        return cls.__count

    @classmethod
    def getBinomialNomenclature(self):
        return self.__binomialNomenclature

    def setHeartChambers(self, heartChambers = 4):
        self._heartChambers = heartChambers
        return True

    def getHeartChambers(self):
        return self._heartChambers

    def __init__(self, name = "Anonymous", furcolor = "Black", commonCall = "Kau", localNames = [], heartChambers = 4):
        super().__init__()
        self.setName(name)
        self.setLocalNames(localNames)
        self.setFurcolor(furcolor)
        self.setCommonCall(commonCall)
        self.setHeartChambers(heartChambers)
        Crow.__count += 1

    def setCommonCall(self, commonCall = "Kau"):
        self._commonCall = commonCall
        return True

    def getCommonCall(self):
        return self._commonCall

    def setFurcolor(self, furcolor = "Black"):
        self._furcolor = furcolor
        return True

    def getFurcolor(self):
        return self._furcolor

    def getName(self):
        return self._name
        
    def setName(self, name = "Anonymous"):
        self._name = name
        return True

    def setLocalNames(self, localNames = []):
        self._localNames = localNames
        return True

    def getLocalNames(self):
        return self._localNames

    def isEatable(self):
        return True

    def isFriend(self):
        return True
    
    def isAquatic(self):
        return False

    def isFlyable(self):
        return True

    def __str__(self):
        return "Crow"

__author__ = 'Jorge Monardes'

class EverisCollaborator:

    company = 'Everis NTT Data'

    def __init__(self, name, skills, sleepingHours):
        self.name = name
        self.skills = skills
        self.sleepingHours = sleepingHours

    def profile(self):
        print("nombre: %s, principal habilidad: %s, " \
              "horas diarias de sueño %d" % (self.name, self.skills[0], self.sleepingHours))

    def addSkill(self, skill):
        self.skills.append(skill)


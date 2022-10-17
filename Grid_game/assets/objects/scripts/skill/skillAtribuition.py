from assets.objects.scripts.skill.skill import Skill
from assets.objects.scripts.skill.slash import Slash
import os.path


class SkillAtribuition:

    def __init__(self, classe: str) -> None:
        self._SkillList = []
        self.__path = os.path.join('assets/objects/scripts/system/db')
        self.__attribuition(classe)

    def __attribuition(self, classe: str) -> None:
        if classe == 'thief':
            self.__path = os.path.join(self.__path, 'tf.sav')
            db = []
            try:
                db = open(self.__path, 'r')
            except Exception as e:
                print(e)
            for line in db:
                self._SkillList.append(self.__chose_skill(int(line)))
            db.close()
        elif classe == 'adventurer':
            self.__path = os.path.join(self.__path, 'ad.sav')
            db = []
            try:
                db = open(self.__path, 'r')
            except Exception as e:
                print(e)
            for line in db:
                self._SkillList.append(self.__chose_skill(int(line)))
            db.close()
        elif classe == 'student':
            self.__path = os.path.join(self.__path, 'sm.sav')
            db = []
            try:
                db = open(self.__path, 'r')
            except Exception as e:
                print(e)
            for line in db:
                self._SkillList.append(self.__chose_skill(int(line)))
            db.close
        elif classe == 'archer':
            self.__path = os.path.join(self.__path, 'ac.sav')
            db = []
            try:
                db = open(self.__path, 'r')
            except Exception as e:
                print(e)
            for line in db:
                self._SkillList.append(self.__chose_skill(int(line)))
            db.close()

    def __chose_skill(self, id: int) -> Skill:
        if id == 1:
            return Slash(0, 0)

    def get_Skill_List(self) -> list:
        return self._SkillList

import random


class Sequence:
    # name - название последовательности, string
    # seq - последовательность, string
    def __init__(self, name, seq):
        self._name = name
        self._seq = seq
        if not hasattr(self, '_alphabet'):
            self._alphabet = dict(zip(set(seq), [0] * len(set(seq))))

    # возвращает частоты встречаемости символов в последовательности, dict = {alpha:freq}
    def frequencies(self):
        self._frequencies = {sym: self._seq.count(sym) for sym in self._alphabet}
        return self._frequencies

    # возвращает массу последовательности, float
    def weight(self):
        self.frequencies()
        return sum([num * count for num, count in zip(self._alphabet.values(), self._frequencies.values())])

    # вовзращает алфавит последовательности, string
    @property
    def alphabet(self):
        return ''.join(self._alphabet.keys())

    @classmethod
    def get_alphabet(cls):
        return ''.join(cls._alphabet.keys())

    # возвращает название последовательности, string
    def get_name(self):
        return self._name

    # возвращает последовательность, string
    def get_sequence(self):
        return self._seq

    # возвращает длину последовательности, int
    def length(self):
        return len(self._seq)


# ДНК
class DNA(Sequence):
    _complementary_dict = dict(zip('ATGC', 'TACG'))
    _transcription_dict = dict(zip('ATGC', 'UACG'))
    _alphabet = {'A': 135.13, 'T': 126.11334, 'G': 151.13, 'C': 111.102}

    def __init__(self, name, seq):
        super().__init__(name, seq)

    # возвращает комплементарную последовательность
    # если существует словарь комплементарности - иначе: возвращает ту же последовательность
    def complementary(self):
        return ''.join(map(lambda x: self._complementary_dict[x], self._seq))

    def transcription(self):
        return RNA(f'Transcripted from {self._name}',
                   ''.join(map(lambda x: self._transcription_dict[x], self._seq)))


# РНК
class RNA(Sequence):
    _alphabet = {'A': 135.13, 'U': 112.08676, 'G': 151.13, 'C': 111.102}
    _translation_dict = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                         'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                         'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                         'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                         'UAU': 'Y', 'UAC': 'Y', 'UAA': 'stop', 'UAG': 'stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
                         'CAG': 'Q',
                         'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                         'UGU': 'C', 'UGC': 'C', 'UGA': 'stop', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R',
                         'CGG': 'R',
                         'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
                         'GGG': 'G', }

    def __init__(self, name, seq):
        super().__init__(name, seq)

    def translation(self):
        if len(self._seq) % 3 != 0:
            raise ValueError("Длина цепи РНК не кратна 3. Белок не собран")
        else:
            self.__i = 0
            self.__protein = []
            self.__codon = ''
            while self.__i + 3 <= self.length():
                self.__codon = self._seq[self.__i:self.__i + 3]

                if self._translation_dict[self.__codon] != 'stop':
                    self.__protein.extend(self._translation_dict[self.__codon])
                    self.__i += 3

            return Protein(f'Translated from {self._name}',
                           ''.join(self.__protein))


class Protein(Sequence):
    _alphabet = {'G': 75.0669, 'L': 131.1736, 'Y': 181.1894, 'S': 105.093, 'E': 147.1299,
                 'Q': 146.1451, 'D': 133.1032, 'N': 132.1184, 'F': 165.19, 'A': 89.0935,
                 'K': 146.1882, 'R': 174.2017, 'H': 155.1552, 'C': 121.159, 'V': 117.1469,
                 'P': 115.131, 'W': 204.2262, 'I': 131.1736, 'M': 149.2124, 'T': 119.1197}

    def __init__(self, name, seq):
        super().__init__(name, seq)


if __name__ == '__main__':
    obj = DNA('dna', 'AAATCG')
    tab = 15
    print('Name:'.ljust(tab), obj.get_name())
    print('Sequence:'.ljust(tab), obj.get_sequence())
    print('Complementary:'.ljust(tab), obj.complementary())
    print('Weight_DNA:'.ljust(tab), obj.weight())
    obj1 = obj.transcription()
    print('Transcription:'.ljust(tab), obj1.get_sequence())
    print('Weight_RNA:'.ljust(tab), obj1.weight())
    obj2 = obj1.translation()
    print('Translation:'.ljust(tab), obj2.get_sequence())
    print('Weight_pro:'.ljust(tab), obj2.weight())


###############  генератор элементов  ###############
def generator_element(choise):
    result = random.choice(str(choise.alphabet))
    return result

################  генератор последовательностей (random.choices) случайной длины  ------------
def generator_seq_r(choise):
    result = random.choices(str(choise.alphabet), k = random.randint(10, 1000))
    return ''.join(result)

################  генератор последовательностей (random.choices) определенной длины  ------------
def generator_seq(choise,len_seq):
    result = random.choices(str(choise.alphabet), k = len_seq)
    return ''.join(result)

#######********  генератор последовательностей из моей функции определенной длины  ------------
def generator_seq_my(choise,len_seq):
    result = []
    for i in range (0, len_seq):
        gen_element = generator_element(choise)
        result.append (gen_element)
    return ''.join(result)

#######******  генератор последовательностей из моей функции случайной длины  ------------
def generator_seq_r_my(choise):
    result = []
    k = random.randint(10, 1000)
    for i in range (0, k ):
        gen_element = generator_element(choise)
        result.append (gen_element)
    return ''.join(result)

if __name__ == '__main__':
    choise_generator = int(input("\nВыберите генератор:\n"
                       "1 - Генератор элементов\n"
                       "2 - Генератор последовательностей (random.choices) случайной длины\n"
                       "3 - Генератор последовательностей (random.choices) определенной длины\n"
                       "4 - Генератор последовательностей из моей функции определенной длины\n"
                        "5 - Генератор последовательностей из моей функции случайной длины\n"))

    if  choise_generator == 1:
        choise = int(input("\nГенератор элементов\n"
                           "Выберите, что сгенерировать:\n"
                           "1 - нуклеотид ДНК\n"
                           "2 - нуклеотид РНК\n"
                           "3 - аминокислота\n"))
        if choise == 1:
            choise = obj
            print("Нуклеотид ДНК: ", generator_element(choise))

        elif choise == 2:
            choise = obj1
            print("Нуклеотид РНК: ", generator_element(choise))

        elif choise == 3:
            choise = obj2
            print("Аминокислота: ", generator_element(choise))


    elif choise_generator == 2:
            choise = int(input("\nГенератор последовательностей (random.choices) случайной длины\n"
                           "Выберите, что сгенерировать:\n"
                           "1 - последовательность ДНК\n"
                           "2 - последовательность РНК\n"
                           "3 - последовательность аминокислот\n"))
            if choise == 1:
                choise = obj
                print("последовательность ДНК: ", generator_seq_r(choise))

            elif choise == 2:
                choise = obj1
                print("последовательность РНК: ", generator_seq_r(choise))

            elif choise == 3:
                choise = obj2
                print("последовательность аминокислот: ", generator_seq_r(choise))

    elif choise_generator == 3:

        choise = int(input("\nГенератор последовательностей (random.choices) определенной длины\n"
                           "Выберите, что сгенерировать:\n"
                           "1 - последовательность ДНК\n"
                           "2 - последовательность РНК\n"
                           "3 - последовательность аминокислот\n"))
        len_seq = int(input("Длина последовательности:\n"))
        if choise == 1:
            choise = obj
            print("последовательность ДНК: ", generator_seq(choise, len_seq))

        elif choise == 2:
            choise = obj1
            print("последовательность РНК: ", generator_seq(choise, len_seq))

        elif choise == 3:
            choise = obj2
            print("последовательность аминокислот: ", generator_seq(choise, len_seq))




    elif choise_generator == 4:
        choise = int(input("\nГенератор последовательностей из моей функции определенной длины\n"
                           "Выберите, что сгенерировать:\n"
                           "1 - последовательность ДНК\n"
                           "2 - последовательность РНК\n"
                           "3 - последовательность аминокислот\n"))
        len_seq = int(input("Длина последовательности:\n"))
        if choise == 1:
            choise = obj
            print("Последовательность ДНК: ", generator_seq_my(choise, len_seq))

        elif choise == 2:
            choise = obj1
            print("Последовательность РНК: ", generator_seq_my(choise, len_seq))

        elif choise == 3:
            choise = obj2
            print("Последовательность аминокислот: ", generator_seq_my(choise, len_seq))


    elif choise_generator == 5:
        choise = int(input("\nГенератор последовательностей из моей функции случайной длины\n"
                           "Выберите, что сгенерировать:\n"
                           "1 - последовательность ДНК\n"
                           "2 - последовательность РНК\n"
                           "3 - последовательность аминокислот\n"))

        if choise == 1:
            choise = obj
            print("Последовательность ДНК: ", generator_seq_r_my(choise))

        elif choise == 2:
            choise = obj1
            print("Последовательность РНК: ", generator_seq_r_my(choise))

        elif choise == 3:
            choise = obj2
            print("Последовательность аминокислот: ", generator_seq_r_my(choise))

class CpfCnpjUtil:
    def __init__(self, doc: str):
        self.doc = doc
        self.doc = self.unformat()
    
    def unformat(self):
        if not self.doc:
            return ''
        unformatted = ''.join(filter(str.isdigit, self.doc))
        if len(unformatted) in [11, 14]:
            return unformatted
        if len(unformatted) < 11:
            return unformatted.zfill(11)
        elif len(unformatted) < 14:
            return unformatted.zfill(14)
        return unformatted
    
    def format(self):
        unformatted = self.unformat()
        if len(unformatted) == 11:
            return f'{unformatted[:3]}.{unformatted[3:6]}.{unformatted[6:9]}-{unformatted[9:]}'
        elif len(unformatted) == 14:
            return f'{unformatted[:2]}.{unformatted[2:5]}.{unformatted[5:8]}/{unformatted[8:12]}-{unformatted[12:]}'
        return self.doc


    def validate(self):
        unformatted = self.unformat()
        if len(unformatted) == 11:
            return self._validate_cpf(unformatted)
        elif len(unformatted) == 14:
            return self._validate_cnpj(unformatted)
        return False

    def _validate_cpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        for i in range(9, 11):
            value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != int(cpf[i]):
                return False
        return True

    def _validate_cnpj(self, cnpj):
        if len(cnpj) != 14 or not cnpj.isdigit():
            return False
        weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(12, 14):
            value = sum((int(cnpj[num]) * weights[num + 1 - i] for num in range(0, i)))
            digit = (value % 11)
            if digit < 2:
                digit = 0
            else:
                digit = 11 - digit
            if digit != int(cnpj[i]):
                return False
        return True

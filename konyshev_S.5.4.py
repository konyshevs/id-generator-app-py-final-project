def check_id_valid(id_number):
    """
    This function checks if ID number is valid.
    :param id_number: ID number to check.
    :type id_number: int
    :return: bool
    :rtype: bool
    """
    count = 0
    first_step = []
    second_step = []
    for num in str(id_number):  # first step
        count += 1
        if count % 2 == 0:
            first_step.append(int(num) * 2)
        else:
            first_step.append(int(num))

    for num in first_step:  # second step
        if num > 9:
            second_step.append(sum([int(x) for x in str(num)]))
        else:
            second_step.append(num)

    return sum(second_step) == 10  # third step


class IDIterator:
    """
    A class used to create an iterator of valid ID numbers
    """

    def __init__(self, id):
        """
        This method initialize ID number.
        :param id: ID number to initialize.
        :type id: int
        :return: none
        """
        self._id = id

    def __iter__(self):
        """
        This method return self.
        :return: self
        """
        return self

    def __next__(self):
        """
        This method generate next valid ID number.
        :raise: StopIteration: raises an Exception
        :return: next valid ID number
        :return type: int
        """
        while True:
            self._id += 1
            if check_id_valid(self._id):
                break
        if self._id > 999999999 or self._id < 99999999:
            raise StopIteration()

        return self._id


def id_generator(id):
    """
    This function creates a generator of valid ID numbers.
    :param id: ID number to start.
    :type id: int
    :return: next valid ID number
    :rtype: gen
    """
    while 99999999 < id < 999999999:
        id += 1
        if check_id_valid(id):
            yield id


def main():
    input_id = int(input('Enter ID: '))
    method = input('Generator or Iterator? (gen/it)? ')
    try:
        if method == 'it':
            id_iter = IDIterator(input_id)
            for i in range(10):
                print(next(id_iter))

        elif method == 'gen':
            id_gen = id_generator(input_id)
            for i in range(10):
                print(next(id_gen))

        else:
            print('Invalid input!')
    except StopIteration:
        print('No more options or out of range')


if __name__ == '__main__':
    main()

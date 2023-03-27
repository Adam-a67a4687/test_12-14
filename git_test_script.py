class Transformator:
    def __init__(self, geoid: str) -> None:
        self.geoid = geoid

    def transform(self):
        x = 300
        y = 701
        return x + y
    
    def display_geoid(self):
        print(f'{self.geoid}')
        return f'This is our geoid: {self.geoid}'
    
if __name__ == '__main__':
    transformator = Transformator('WGS84')
    transformator.transform()

class Transformator:
    def __init__(self, geoid: str) -> None:
        self.geoid = geoid

    def transform():
        x = 300
        y = 700
        return x + y
    
    def display_geoid(self):
        print(f'{self.geoid}')
        return self.geoid
    
if __name__ == '__main__':
    transformator = Transformator('WGS84')
    transformator.transform()

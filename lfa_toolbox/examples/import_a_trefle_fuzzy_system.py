from lfa_toolbox.trefle.tffconverter import TffConverter
from lfa_toolbox.view.fis_viewer import FISViewer


def main():
    # Assuming you have run Trefle and saved the fuzzy model as 'demo_fis.tff'
    tff_str = open("demo_fis.tff").read()

    # Convert the tff model into a SingletonFIS instance
    fis = TffConverter.to_fis(tff_str)

    # Then you can play with it the same way you would with a SingletonFIS
    # instance. For example let's print the first rule.
    print(fis.rules[0])

    # And you can of course visualize the fuzzy system with FISViewer since
    # it is a regular SingletonFIS.
    fis_viewer = FISViewer(fis)
    fis_viewer.show()


if __name__ == '__main__':
    main()

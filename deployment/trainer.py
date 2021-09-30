import argparse
import logging

logging.basicConfig(filename='../logs/trainer.log', filemode='w', level=logging.DEBUG)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    arguments = parser.parse_args()
    model_output_path = arguments.output
    logging.info(f'Input path: {arguments.input}')
    logging.info(f'Output path: {arguments.output}')





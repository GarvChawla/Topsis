from topsis import calculate_topsis
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Incorrect number of arguments.")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 102203753.py 102203753-data.csv \"1,1,1,2\" \"+,+,-,+\" 102203753-result.csv")
        sys.exit(1)
    
    try:
        calculate_topsis(*sys.argv[1:])
        print(f"Results saved to {sys.argv[4]}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
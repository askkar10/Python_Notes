# zapisywanie i otwieranie za pomocą funkcji
import pickle
def save_data(data_dict):
  with open('state2','wb') as file:
    pickle.dump(data_dict,file)

def restore_data():
  with open('state2','rb') as file:
    data_dict = pickle.load(file)
  return data_dict

if __name__ == '__main__':
  data_dict = {'a':42,
               'b':3.14,
               'c':'test'}

save_data(data_dict)
restored_data = restore_data()
print(restored_data)
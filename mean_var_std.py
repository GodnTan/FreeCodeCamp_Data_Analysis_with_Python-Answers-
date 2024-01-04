import numpy as np
def calculate(list):
  if (len(list) != 9):
    raise ValueError( "List must contain nine numbers.")
  data = np.reshape(np.array(list),(3,3))
  ans={}
  ans['mean'] = [np.mean(data,axis=0).tolist(),
                 np.mean(data,axis=1).tolist(),
                 np.mean(data.flatten()).tolist()]
  ans['variance'] =[np.var(data, axis=0).tolist(), 
                    np.var(data, axis=1).tolist(),       
                    np.var(data.flatten()).tolist()]
  ans['standard deviation'] = [np.std(data, axis=0).tolist(),           
                               np.std(data, axis=1).tolist(), 
                               np.std(data.flatten()).tolist()]
  ans['max'] = [np.max(data, axis=0).tolist(), 
                np.max(data, axis=1).tolist(), 
                np.max(data.flatten()).tolist()]
  ans['min'] = [np.min(data, axis=0).tolist(),
                np.min(data, axis=1).tolist(), 
                np.min(data.flatten()).tolist()]
  ans['sum'] = [np.sum(data, axis=0).tolist(),
                np.sum(data, axis=1).tolist(), 
                np.sum(data.flatten()).tolist()]
  return ans

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if i in ds:
                ds[i] = ds.get(i)+1
            else:
                ds[i] = 1
        for j in t:
                    if j in dt:
                        dt[j] = dt.get(j)+1
                    else:
                        dt[j] = 1
        print(ds)
        print(dt)
        flag = True
        for k in ds:
            #  if k in dt:
            #       print(k," found with value: ",ds[k])
            #  else:
            #     print("Not found")
             if (k in dt) and (dt[k]==ds[k]):
                  flag = True
             else:
                flag = False
                return flag
        for l in dt:
             if (l in ds) and (ds[l]==dt[l]):
                  flag = True
             else:
                  flag = False
                  return flag
        return flag
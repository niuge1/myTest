import scipy.io
import math
f = scipy.io.loadmat("./Originaldata_separate.mat")
f_list = list(f["Originaldata_separate"])
time_shaft = []
org_meter = []

for data in f["Originaldata_separate"]:
    time_shaft.append(data[0])
    org_meter.append(data[1])

time_interval=60                       # 设定分精度时间间隔,以分钟为单位
start_time=math.ceil(time_shaft[0]*24*60/time_interval)/(24*60/time_interval)                     # 分精度的开始时间
stop_time=math.floor(time_shaft[len(time_shaft)-1]*24*60/time_interval)/(24*60/time_interval)    # 分精度的结束时间

# 分精度时间轴
# time_shaft2=start_time:(1/(24*60/time_interval)):stop_time
t = start_time
time_shaft2 = []
while t <= stop_time:
    time_shaft2.append(t)
    t += 1/(24*60/time_interval)
org_meter2 = dict()                                                                                  # 分精度的电表累计读数
org_flag2 = dict()                                                                                   # 分精度的数据类型标记
time_shaft_round = [round(i*24*60/time_interval)/(24*60/time_interval) for i in time_shaft]      # round(time_shaft*24*60/time_interval)/(24*60/time_interval)
temp = [time_shaft[i]-time_shaft_round[i] for i in range(0, len(time_shaft))]
time_shaft_adj = [time_shaft_round, temp]
# 分精度
kk = 0
for j in range(0, len(time_shaft2)):
    meter_temp = dict()
    diff_temp = dict()
    l=0 # 各分精度时间单元内的点数
    # 按分精度时间轴归类原时间轴
    # for k=kk+1:size(time_shaft_round,1)
    for k in range(kk, len(time_shaft_round)):
        if time_shaft_round[k] - time_shaft2[j] < -0.000001:
            kk=kk+1
        elif time_shaft_round[k] - time_shaft2[j] >= -0.000001 and time_shaft_round[k] - time_shaft2[j] <= 0.000001:
            meter_temp[l] = org_meter[k] # 有问题
            diff_temp[l] = time_shaft_adj[0][k]
            l = l+1
            kk = kk+1
        elif time_shaft_round[k] - time_shaft2[j] > 0.000001:
            break

    if l==0:                         # 如果该分精度时间单元内没有原时间点,表累计值赋值-9999
        org_meter2[j] = -9999 # 有问题
        org_flag2[j] = 1  #有问题
    elif l == 1:                    # 如果该分精度时间单元内只有一个原时间点,表累计值为该原时间点的值
        org_meter2[j] = meter_temp[0]
        if meter_temp[0] < 0:
            org_flag2[j] = 1
        else:
            org_flag2[j] = 0
    elif diff_temp[0] >= 0:     # 如果多于两个原时间点在该分精度时间单元内,判断是否原时间点都在份精度点的一侧还是两侧
        org_meter2[j] = meter_temp[0]
        if meter_temp[0] < 0:
            org_flag2[j] = 1
        else:
            org_flag2[j] = 0
    elif diff_temp[l] <= 0:
            org_meter2[j] = meter_temp[l]    # 如果在一侧，取最靠近点
            if meter_temp[l] < 0:
                org_flag2[j] = 1
            else:
                org_flag2[j] = 0
    else:
        for m in range(0, l-1):
            if diff_temp[m]*diff_temp[m+1] <= 0:       # 如果在两侧，取临近两点的线性差值
                org_meter2[j] = meter_temp[m] - (meter_temp[m+1] - meter_temp[m]) * diff_temp[m]/(diff_temp[m+1]- diff_temp[m])
                if meter_temp[m] < 0 or meter_temp[m+1] < 0:
                    org_flag2[j] = 1
                else:
                    org_flag2[j] = 0
                break

print(org_meter2)
print(org_flag2)
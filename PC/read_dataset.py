from avalanche.benchmarks.classic import CORe50, OpenLORIS, CLStream51

## CORe50
dataset = CORe50(scenario="nc", mini=True) # original 128x128, mini 32x32
# scenario : nbatches
# "ni": 8, "nc": 9, "nic": 79, "nicv2_79": 79, "nicv2_196": 196, "nicv2_391": 391
### 새로운 시나리오 적용 시 avalanche.benchmarks.classic.{해당 데이터}.py에서 시나리오에따라 파일 경로 list 설정하는 부분 수정 or 추가

## OpenLORIS
dataset = OpenLORIS(factor="clutter")
# scenario : nbatches
# "clutter": 9, "illumination": 9, "occlusion": 9, "pixel": 9, "mixture-iros": 12

## Stream51
dataset = CLStream51(scenario="class_instance", bbox_crop=True) 
# scenario
# "iid", "class_iid", "instance", "class_instance"

train_stream = dataset.train_stream
test_stream = dataset.test_stream

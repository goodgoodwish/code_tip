
## 5. Bit manipulation

### Update bit

```python

def update_bit(num, i, bit_value):
  mask = ~(1 << i)
  new_num = (num & mask) | (bit_value << i)
  return new_num

7 = 111, 
update_bit(7, 1, 0)  # 5: 101

2 = 010,
update_bit(2, 1, 0)

```

```scala
def updateBit(num:Int, i:Int, bitValue:Int):Int = {
  val mask = ~(1 << i)
  val newNum = (num & mask) | (bitValue << i)
  newNum
}

updateBit(2, 1, 0) // 010 -> 000

```

## 7. Object Oriented Design

* Singleton class
```python
```
+ Factory method


## 8. Recursion and Dynamic programming


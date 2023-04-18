import Quaternion
import From_string_to_binary
import binary_arithmetic
import From_binary_to_string

quaternion_add = Quaternion.quaternion_add
quaternion_multiply = Quaternion.quaternion_multiply
fromStringToBinary = From_string_to_binary.fromStringToBinary
add_binaries = binary_arithmetic.add_binaries
subtract_binaries = binary_arithmetic.subtract_binaries
fromBinaryToString = From_binary_to_string.fromBinaryToString

M = [1, 1, 1, 1]
S = [1, 7, 2, 1]
L = [2, 3, 6, 3]


# p(x) = x + 4
# q(x) = 3*x^2 + 5
# t(x) = x^3+2*x+2
# r(x) = 7*x + 1

pM = [5, 1, 1, 1] #p(M)
tS = quaternion_add(quaternion_add(quaternion_multiply(S, quaternion_multiply(S, S)), quaternion_multiply([2, 0, 0, 0], S)), [2, 0, 0, 0]) #t(S)
qM = quaternion_add(quaternion_multiply([3, 0, 0, 0], quaternion_multiply(M, M)), [5, 0, 0, 0])
rS = quaternion_add(quaternion_multiply([7, 0, 0, 0], S), [1, 0, 0, 0])

A = quaternion_multiply(quaternion_multiply(pM, L), tS)
B = quaternion_multiply(quaternion_multiply(qM, L), rS)

print("A =", A)
print("B =", B)

kA = quaternion_multiply(quaternion_multiply(pM, B), tS)
kB = quaternion_multiply(quaternion_multiply(qM, A), rS)

print("kA = {0}".format(kA))
print("kB = {0}".format(kB))

#Alice encrypts her message, which is "Hello, Bob."
alice_message = input("Enter Alice's message to Bob: ")
print("Alice's message: ", alice_message)

messageBinary = fromStringToBinary(alice_message)
print("The message has been converted to a binary: ", messageBinary)

sumKA = 0
for i in range(4):
    sumKA += kA[i]

kABinary = bin(sumKA) # has '0b'
kABinary = kABinary[kABinary.index('b')+1:] # pure binary number
print("kA (the key) has been converted to a binary: ", kABinary)

finalEncryptedMessage = add_binaries(messageBinary, kABinary)
print("Final encrypted message sent to Bob: ", finalEncryptedMessage)

# Bob decrypts the message sent by Alice"
sumKB = 0
for i in range(4):
    sumKB += kB[i]

kBBinary = bin(sumKB) # has '0b'
kBBinary = kBBinary[kBBinary.index('b')+1:] # pure binary number
print("Bob's key converted to a binary: ", kBBinary)

m = "0" + subtract_binaries(finalEncryptedMessage, kBBinary)
decryptedMessage = fromBinaryToString(m)
print("Decrypted message by Bob: ", decryptedMessage)


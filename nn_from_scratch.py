#!/usr/bin/python

import torch

num_input = 2
num_hidden = 16
num_output = 1
num_layers = 1

lr = 0.1

t_weights_1 = torch.randn(num_hidden,num_input)
t_weights_2 = torch.randn(num_output,num_hidden)

t_bias_1 = torch.randn(1,num_hidden)
t_bias_2 = torch.randn(1,num_output)

Y1 = t_weights_1

def forward(X):
	global Y1
	Y = torch.matmul(t_weights_1, torch.t(X))# + t_bias_1
	Y1 = sigmoid(Y)
	Z = torch.matmul(t_weights_2, Y1)# + t_bias_2
	Z1 = sigmoid(Z)
	return Z1

def backprop(X,y,f):
	global t_weights_2
	global t_weights_1
	global Y1
	cost = y - f
	cost_delta = cost * sigmoid_prime(f)
	Y1_error = torch.matmul(torch.t(t_weights_2), cost_delta)
	Y1_delta = Y1_error * sigmoid_prime(Y1)
	t_weights_1 += lr*torch.matmul(Y1_delta, X)
	t_weights_2 += lr*torch.matmul(cost_delta, torch.t(Y1))


def sigmoid(x):
	y = 1/(1+torch.exp(-x))
	return y

def sigmoid_prime(x):
	y = x*(1-x)
	return y

def train_network(X,y):
	f = forward(X)
	backprop(X,y,f)

def loss_function(X,y):
	loss = torch.mean((y - forward(X))**2).detach().item()
	#print("y is ",y,"pred is ",forward(X))
	return loss


f1 = open("train.txt","r")
lines = f1.readlines()
f1.close()

f2 = open("test.txt","r")
lines2 = f2.readlines()
f2.close()


def run_training():
	count = 0
	best_success_rate = 0
	for k in lines:
		total_loss = 0
		count += 1
		A = k.split(",")
		X = torch.tensor([[float(A[0].strip()), float(A[1].strip())]])
		y = torch.tensor([[float(A[-1].strip())]])
		f = forward(X)
		backprop(X,y,f)
		
		count_success = 0
		for n in lines2:
			B = n.split(",")
			X_test = torch.tensor([[float(B[0].strip()), float(B[1].strip())]])
			y_test = int(B[-1].strip())
			pred = forward(X_test)
			result = 0
			if pred <= 0.5:
				result = 0
			else:
				result = 1
			if result == y_test:
				count_success += 1

		#print(count, (count_success/50))

		if count_success/50 > best_success_rate:
			best_success_rate = count_success/50
			
		print(count, (count_success/50))

	print("Best success score : ",best_success_rate)
	print(t_weights_1)
	print(t_weights_2)

run_training()
	

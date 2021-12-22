import axiosInstance from './index'


const axios = axiosInstance

export const getBooks=() => {return axios.get('http://localhost:8000/api/loginUser/')}

//export const postBook =(bookName,bookAuthor) => {return axios.post('http://localhost:8000/api/books/'),{'name':bookName,'author':bookAuthor}}

/*
export const postBook =(userName,passWord) => {
	return axios({
		method:'post',
		url:'http://localhost:8000/api/loginUser/',
		data:{'name':bookName,'':bookAuthor}
	});
}*/
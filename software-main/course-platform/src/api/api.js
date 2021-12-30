import axios from './index'

const api = {
  getUser: () => { return axios.get('/api/loginUser/') },
  login: (user_info) => { return axios.post('/api/login/', user_info) },
  signup: (user_info) => { return axios.post('/api/register/', user_info) },
  getTeachClass: (username) => { return axios.post('/api/getbanjiList/', {'username': username}) },
  getStudyClass: (username) => { return axios.post('/api/getclassList/', {'username': username}) },
  quiteClass: (username, classId) => {return axios.post('/api/quitclass/', {'username': username, 'classId': classId})},
  getClassStudentInfo: (classId) => {return axios.post('/api/getclassStudentList/', {'classId': classId})},
  deleteClass: (classId) => {return axios.post('/api/deleteClass/', {'classId': classId})},
  deleteLesson: (lessonId) => {return axios.post('/api/deleteLesson/', {'lessonId': lessonId})},
  getClassMessage: (classId) => {return axios.post('/api/getClassMessage/', {'classId': classId})}
}

export default api;
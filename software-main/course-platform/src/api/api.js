import axios from './index'

const api = {
  getUser: () => { return axios.get('/api/loginUser/') },
  login: (user_info) => { return axios.post('/api/login/', user_info) },
  signup: (user_info) => { return axios.post('/api/register/', user_info) },
  getTeachClass: (username) => { return axios.post('/api/getbanjiList/', { 'username': username }) },
  getStudyClass: (username) => { return axios.post('/api/getclassList/', { 'username': username }) },
  createLesson: (username, createLessonForm) => { return axios.post('/api/createcourse/', { 'teacher': username, 'name': createLessonForm.lessonName, 'simple_name': createLessonForm.lessonSimpleName }) },
  createClass: (createClassForm) => { return axios.post('/api/createbanji/', { 'name': createClassForm.name, 'year': createClassForm.year, 'season': createClassForm.season, 'couid': createClassForm.lessonId, 'color': createClassForm.color }) },
  editLesson: (lessonId, lessonForm) => {return axios.post('/api/editLesson/', {'lessonId': lessonId, 'lessonForm': lessonForm})},
  editClass: (classId, classForm) => {return axios.post('/api/editClass/', {'classId': classId, 'classForm': classForm})},
  joinClass: (username, joinClassForm) => { return axios.post('/api/joinbanji/', { 'username': username, 'code': joinClassForm.classCode }) },
  quitClass: (username, classId) => { return axios.post('/api/quitclass/', { 'username': username, 'classId': classId }) },
  getClassStudentInfo: (classId) => { return axios.post('/api/getclassStudentList/', { 'classId': classId }) },
  deleteClass: (classId) => { return axios.post('/api/deleteClass/', { 'classId': classId }) },
  deleteLesson: (lessonId) => { return axios.post('/api/deleteLesson/', { 'lessonId': lessonId }) },
  getClassMessage: (classId) => { return axios.post('/api/getClassMessage/', { 'classId': classId }) },
  savePersonInfo: (personInfoForm) => {return axios.post('/api/savePersonInfo/', { 'personInfoForm': personInfoForm})}
}

export default api;
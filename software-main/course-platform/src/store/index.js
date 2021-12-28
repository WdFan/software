import { createStore } from 'vuex'

export default createStore({
  state: {
    user_info: JSON.parse(localStorage.getItem("user_info") || '{}'),
    is_login: false,
    home_index_tab: (localStorage.getItem("home_index_tab") || "teach"),
    userTeachData: [],
    userStudyData: []
  },
  mutations: {
    updateUser(state, data) {
      state.user_info = data;
      state.is_login = true;
      localStorage.setItem("user_info", JSON.stringify(data));
      localStorage.setItem("is_login", true);
    },
    updateTab(state, data) {
      state.home_index_tab = data;
      localStorage.setItem("home_index_tab", data);
    },
    clearUser(state) {
      state.user_info = {};
      state.is_login = false;
      state.home_index_tab = "teach"
      state.userTeachData = [];
      state.userStudyData = [];
      localStorage.clear();
    }
  },
  actions: {
  },
  modules: {
  }
})

export default {
  state: {
    pageName: '',
  },
  mutations: {
    SET_PAGE_NAME(state, name) {
      state.pageName = name;
    },
  },
  actions: {
    preparePage(store, { name, isAsync = true }) {
      store.commit('CORE_SET_PAGE_LOADING', isAsync);
      store.commit('SET_PAGE_NAME', name);
      store.commit('CORE_SET_ERROR', null);
    },
    resetModuleState(store, { fromRoute }) {
      const moduleName = pageNameToModuleMap[fromRoute.name];
      if (moduleName) {
        return store.commit(`${moduleName}/RESET_STATE`);
      }
    },
  },
  modules: {},
};

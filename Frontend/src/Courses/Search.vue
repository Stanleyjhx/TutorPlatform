<template>
  <el-autocomplete
    v-model="state"
    :fetch-suggestions="querySearchAsync"
    placeholder="type the course information"
    @select="handleSelect"
  ></el-autocomplete>
</template>

<script>
  export default {
    name: "Search",
    data() {
      return {
        courses: [{
          value: 'Comp421',
          tutor: 'Stephen',
          rating: 3,
          url: '/'
        }, {
          value: 'Comp307',
          tutor: 'Kevin',
          rating: 4,
          url: '/'
        }, {
          value: 'Math223',
          tutor: 'Donald',
          rating: 5,
          url: '/'
        }, {
          value: 'Ecse321',
          tutor: 'Lee',
          rating: 4.3,
          url: '../search'
        }],
        state: '',
        timeout:  null,
        displayList: []
      };
    },
    methods: {
      // these are test data
      loadAll() {
        this.axios.get("/api-course/courses/",{
          headers: { 'Authorization' : 'Token '+ this.$store.state.token}
        })
          .then((response) => {
            let courses = response.data
            for (let course of courses) {
              let courseInfo = {'value': course.subject + '' + course.number,
                'tutor': course.tutor, 'rating': course.rating, 'url': '/'}
              this.displayList.push(courseInfo)
            }
          })
          .catch((error) => {
            console.log(error);
            this.$message.error('Please try again.');
          })
      },
      querySearchAsync(queryString, cb) {
        let courses = this.courses;
        let results = queryString ? courses.filter(this.createStateFilter(queryString)) : courses;

        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 300 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
        this.displayList = [];
        this.displayList.push(item);
        console.log(item);

      }
    },
    // mounted() {
    //   this.courses = this.loadAll();
    // }
  }
</script>

<style scoped>

</style>

<template>
    <div>
        <el-collapse v-model="activeNames" accordion>

            <el-collapse-item title="Post a course" name="1">
                <course @colseCollapseItem="update"></course>
            </el-collapse-item>

            <el-collapse-item title="My courses" name="2" >
                  <el-timeline >
                    <el-dialog title="Edit Course" :visible.sync="dialogVisible">
                        <span>{{subject}} {{number}}</span>
                        <el-form style="margin-top:10px;">
                            <el-form-item >
                            <el-col :span="20" style="text-align: left; margin-bottom:10px;">Is this course available?</el-col>
                            <el-col :span="4">
                                <el-switch
                                    v-model="isAvailable">
                                </el-switch>
                                </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Price</el-col>
                            <el-col :span="20">
                                <el-input v-model="price"/>
                            </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Term</el-col>
                            <el-col :span="20">
                                <el-input v-model="term"/>
                            </el-col>
                            </el-form-item>
                            <el-form-item >
                            <el-col :span="4" style="text-align: left; margin-bottom:10px;">Descript</el-col>
                            <el-col :span="20">
                                <el-input v-model="description"/>
                            </el-col>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button size="mini" @click="deleteCourse">Delete this course</el-button>
                            <el-button size="mini" type="primary" @click="submitEdit">save change</el-button>
                        </div>
                    </el-dialog>

                    <el-timeline-item v-for="course in courses"  v-bind:key="course.id" placement="top">
                    <el-card class="box-card" >
                        <div slot="header" class="clearfix">
                            <span>{{course.subject}} {{course.number}}</span>
                            <el-button @click="editCourse(course)" style="float: right; padding: 3px 0" type="text">Edit</el-button>
                        </div>
                        <el-col :span="12" :xs="24">
                            <el-image :src="course.image" style="width: 300px; height: 200px; margin-bottom: 10px">
                            <div slot="placeholder" class="image-slot">
                                Loading<span class="dot">...</span>
                            </div>
                            </el-image>
                        </el-col>

                        <el-col :span="12" :xs="24">
                            <p class="text item">
                            {{'Term: ' + course.term}}
                            <br>
                            {{'Price: ' + course.price}}
                            <br>
                            {{'Is available: ' + course.isAvailable}}
                            <br>
                            {{'Description: '}}
                              <br>
                              {{course.description}}
                            <br><br>
                            <el-rate
                                v-model= course.rating
                                disabled
                                show-score
                                text-color="#ff9900"
                                score-template="{value}">
                            </el-rate>
                            </p>
                        </el-col>

                    </el-card>
                    </el-timeline-item>
                </el-timeline>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>


<script>
import Course from './Course'
export default {
    data() {
        return {
            course: null,
            courseId:'',
            number : '',
            term: '',
            description: '',
            price:'',
            subject:'',
            isAvailable:true,
            activeNames: ['2'],
            courses: [],
            dialogVisible: false
        }
    },
    methods: {
        editCourse(course){
            this.courseId = course.id,
            this.number = course.number,
            this.term = course.term,
            this.description = course.description,
            this.price = course.price,
            this.subject = course.subject,
            this.isAvailable = course.isAvailable,
            this.dialogVisible = !this.dialogVisible
        },
        deleteCourse(){
            this.dialogVisible = false;
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            instance({
                url: '/api-course/course/'+this.courseId,
                method: "DELETE",
            })
            .then((response) => {
                this.$message({
                    message: 'Deleted sussessfully!',
                    type: 'success'
                });
                this.updateCourse()
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        },
        submitEdit(){
            this.dialogVisible = false
            const userId = this.$store.state.userId
            const instance = this.axios.create({
                headers: {
                    Authorization: 'Token '+ this.$store.state.token,
                    'Content-Type': 'application/json'
                },
            });
            instance({
                url: '/api-course/course/'+this.courseId,
                data: {
                    subject: this.subject,
                    number: this.number,
                    term: this.term,
                    description: this.description,
                    isAvailable: this.isAvailable,
                    price: this.price,
                    tutor: userId
                },
                method: "PATCH",
            })
            .then((response) => {
                this.$message({
                    message: 'Edited sussessfully!',
                    type: 'success'
                });
                this.updateCourse()
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })

        },
        update(activeNames){
            this.activeNames = activeNames
        },
        updateCourse(){
            const userId = this.$store.state.userId
            const instance = this.axios.create({
            headers: {
                Authorization: 'Token '+ this.$store.state.token,
                'Content-Type': 'application/json'
            },
            });
            instance({
                url: '/api-course/courses/',
                method: "get",
            })
            .then((response) => {
                this.courses = []
                for(var course of response.data){
                    if(course.tutor == userId)
                        this.courses.push(course)
                }
            })
            .catch((error) => {
                console.log(error);
                this.$message.error('Please try again.');
            })
        }
    },
    mounted(){
        this.updateCourse()
    },
    watch:{
        activeNames: function () {
            this.updateCourse()
        }
    },
    components:{
        Course
    }
}
</script>

<style>

</style>

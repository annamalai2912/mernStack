// Exercise: Render the list of semester courses using .map()
export default function CourseListExercise() {
  const courses = ["Data Structures", "Database Systems", "Web Technology"];

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h3>Enrolled Courses</h3>
      <ul>
        {/* TODO: Use .map() to render each course as an <li> with a key */}
        {courses.map((course, index) => (
          <li key={index}>{course}</li>
        ))}
      </ul>
    </div>
  );
}

const posts = [
    { id: 1, title: "Post 1", body: "......", userId: 1 },
    { id: 2, title: "Post 2", body: "......", userId: 1 },
    { id: 3, title: "Post 3", body: "......", userId: 2 },
    { id: 4, title: "Post 4", body: "......", userId: 2 },
  ];


let id = 2
const getPost = async (id) => {
  return posts.find((post) => post.id === id)
}

let test = await getPost(id)

console.log(test);
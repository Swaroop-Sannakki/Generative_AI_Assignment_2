// Time Function
// Returns current time in HH:MM format
function getTime(){
  let d = new Date();
  return d.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
}

// Creates a message bubble and appends it to chat
function addMessage(text, sender){

  // Set avatar and name based on sender type
  let avatar = sender == "user" ? "🧑" : "🤖";
  let name = sender == "user" ? "You" : "AI";

  // Message HTML structure
  let msg = `
  <div class="message ${sender}">
    <div class="avatar">${avatar}</div>
    <div>
      <div class="message-header">${name} • ${getTime()}</div>
      <div>${text}</div>
    </div>
  </div>`;

  // Add message to chat container
  $("#messages").append(msg);

  // Auto-scroll to latest message
  $("#messages").scrollTop($("#messages")[0].scrollHeight);
}
// smart replies ( fake )
// Returns AI response based on user input keywords
function getSmartReply(input){

  // Convert input to lowercase for easy matching
  input = input.toLowerCase();

  if(input.includes("summarize"))
    return "Send me your notes and I will summarize them 📄";

  if(input.includes("math"))
    return "Send your math problem, I’ll solve it step by step 🧮";

  if(input.includes("explain"))
    return "Tell me the concept, I’ll explain it clearly 💡";

  if(input.includes("interview"))
    return "Tell me your role, I’ll give interview questions 🎯";

  // Default response if no keyword matches
  return "Tell me more 🤔";
}
 
// Handles sending user message and generating AI reply
function sendMessage(customText = null){

  // Get text either from input or suggestion card
  let text = customText ? customText : $("#input").val().trim();

  // Prevent empty messages
  if(text === "") return;

  // Hide welcome screen after first message
  $("#welcome").hide();

  // Add user message
  addMessage(text, "user");

  // Clear input field
  $("#input").val("");

  // Show typing indicator
  $("#typing").removeClass("d-none");

  // Simulate AI delay (1 second)
  setTimeout(()=>{
    $("#typing").addClass("d-none");

    // Add AI response
    addMessage(getSmartReply(text), "bot");

  }, 1000);
}

// event handlers
// Send button click event
$("#sendBtn").click(() => sendMessage());


// Handle Enter key (send message)
// Shift + Enter allows new line
$("#input").keydown(function(e){
  if(e.key === "Enter" && !e.shiftKey){
    e.preventDefault();
    sendMessage();
  }
});



// Auto-resize textarea + enable/disable send button
$("#input").on("input", function(){

  // Auto adjust height
  this.style.height = "auto";
  this.style.height = this.scrollHeight + "px";

  // Disable send button if input is empty
  $("#sendBtn").prop("disabled", $(this).val().trim() === "");
});


// suggestion cards
// Clicking suggestion card sends predefined message
$(".suggestion").click(function(){
  let text = $(this).find("h6").text();
  sendMessage(text);
});

//sidebar features
// New Chat button clears chat and shows welcome screen
$(".new-chat-btn").click(function(){
  $("#messages").empty();
  $("#welcome").show();
});


// Dark mode toggle (adds/removes 'dark' class)
$("#darkModeBtn").click(function(){
  $("body").toggleClass("dark");
});


// Export chat as text file using Blob API
$("#exportBtn").click(function(){

  // Get all chat text
  let text = $("#messages").text();

  // Create file blob
  let blob = new Blob([text], {type:"text/plain"});

  // Create temporary download link
  let a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "chat.txt";

  // Trigger download
  a.click();
});
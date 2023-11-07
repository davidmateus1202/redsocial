digraph model_graph {
fontname="Roboto";
fontsize=8;
rankdir="TB";
splines=true;
node [fontname="Roboto", fontsize=8, shape="plaintext"];
edge [fontname="Roboto", fontsize=8];
subgraph cluster_social {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>social</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
social_models_Profile [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Profile
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">image</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">ImageField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
social_models_Post [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Post
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">content</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">image</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">ImageField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">likes</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">IntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
social_models_Relationship [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Relationship
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>from_user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>to_user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
social_models_Like [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Like
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>post</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_django_contrib_admin {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.admin</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
django_contrib_admin_models_LogEntry [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      LogEntry
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>content_type</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">action_flag</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">PositiveSmallIntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">action_time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">change_message</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">object_id</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">object_repr</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_django_contrib_auth {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.auth</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
django_contrib_auth_models_AbstractUser [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      AbstractUser<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseUser,PermissionsMixin</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">date_joined</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">email</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">EmailField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">first_name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_active</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_staff</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_superuser</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">last_name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>password</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">username</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
django_contrib_auth_models_Permission [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Permission
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>content_type</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">codename</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
django_contrib_auth_models_Group [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Group
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
django_contrib_auth_models_User [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      User<BR/>&lt;<FONT FACE="Roboto"><I>AbstractUser</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>date_joined</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>email</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>EmailField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>first_name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_active</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_staff</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>is_superuser</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>BooleanField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_login</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>last_name</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>password</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>username</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>CharField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_django_contrib_contenttypes {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.contenttypes</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
django_contrib_contenttypes_models_ContentType [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      ContentType
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>AutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">app_label</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">model</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_django_contrib_sessions {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>django.contrib.sessions</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
django_contrib_sessions_base_session_AbstractBaseSession [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      AbstractBaseSession
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">expire_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">session_data</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
django_contrib_sessions_models_Session [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Session<BR/>&lt;<FONT FACE="Roboto"><I>AbstractBaseSession</I></FONT>&gt;
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I><B>session_key</B></I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I><B>CharField</B></I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>expire_date</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>DateTimeField</I></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><I>session_data</I></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><I>TextField</I></FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_chat {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>chat</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
chat_models_Room [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Room
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">name</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_categoria {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>categoria</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
categoria_models_Categoria [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Categoria
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">descripcion</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nombre_categoria</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">slug</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">SlugField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_store {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>store</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
store_models_PerfilVentas [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      PerfilVentas
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>OneToOneField (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">biografia_venta</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">descripcion_venta</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nombre_vendedor</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
store_models_Producto [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Producto
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>categoria</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">created_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">descripcion</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">TextField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">is_available</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">modified_date</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">nombre_producto</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">precio</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">IntegerField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">product_image</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">ImageField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">slug</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">SlugField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">stock</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">IntegerField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_comentarios {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>comentarios</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
comentarios_models_Comentarios [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Comentarios
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>post</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>user</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">text</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">time</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

subgraph cluster_tarjetas {
color=olivedrab4;
label=<
          <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER">
          <FONT FACE="Roboto" COLOR="Black" POINT-SIZE="10">
          <B>tarjetas</B>
          </FONT>
          </TD></TR>
          </TABLE>
          >;
style="rounded";
tarjetas_models_Cart [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      Cart
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">ahora_agregado</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">DateTimeField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto">cart_id</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto">CharField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
tarjetas_models_CartItem [label=<
      <TABLE BGCOLOR="white" BORDER="1" CELLBORDER="0" CELLSPACING="0">
      <TR><TD COLSPAN="2" CELLPADDING="5" ALIGN="CENTER" BGCOLOR="#1b563f">
      <FONT FACE="Roboto" COLOR="white" POINT-SIZE="10"><B>
      CartItem
      </B></FONT></TD></TR>
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>id</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>BigAutoField</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto"><B>cart</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>producto</B></FONT>
      </TD><TD ALIGN="LEFT">
      <FONT COLOR="#7B7B7B" FACE="Roboto"><B>ForeignKey (id)</B></FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">activo</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">BooleanField</FONT>
      </TD></TR>
    
    
    
      <TR><TD ALIGN="LEFT" BORDER="0">
      <FONT FACE="Roboto">cantidad</FONT>
      </TD><TD ALIGN="LEFT">
      <FONT FACE="Roboto">IntegerField</FONT>
      </TD></TR>
    
    
      </TABLE>
      >];
}

social_models_Profile -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=none, dir=both, label=" user (profile)"];
social_models_Post -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (posts)"];
social_models_Relationship -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" from_user (relationships)"];
social_models_Relationship -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" to_user (related_to)"];
social_models_Like -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (user_likes)"];
social_models_Like -> social_models_Post  [arrowhead=none, arrowtail=dot, dir=both, label=" post (post_likes)"];
django_contrib_admin_models_LogEntry -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (logentry)"];
django_contrib_admin_models_LogEntry -> django_contrib_contenttypes_models_ContentType  [arrowhead=none, arrowtail=dot, dir=both, label=" content_type (logentry)"];
django_contrib_auth_base_user_AbstractBaseUser [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">AbstractBaseUser</FONT>
  </TD></TR>
  </TABLE>
  >];
django_contrib_auth_models_AbstractUser -> django_contrib_auth_base_user_AbstractBaseUser  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_auth_models_PermissionsMixin [label=<
  <TABLE BGCOLOR="white" BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="#1b563f">
  <FONT FACE="Roboto" POINT-SIZE="12" COLOR="white">PermissionsMixin</FONT>
  </TD></TR>
  </TABLE>
  >];
django_contrib_auth_models_AbstractUser -> django_contrib_auth_models_PermissionsMixin  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_auth_models_Permission -> django_contrib_contenttypes_models_ContentType  [arrowhead=none, arrowtail=dot, dir=both, label=" content_type (permission)"];
django_contrib_auth_models_Group -> django_contrib_auth_models_Permission  [arrowhead=dot, arrowtail=dot, dir=both, label=" permissions (group)"];
django_contrib_auth_models_User -> django_contrib_auth_models_Group  [arrowhead=dot, arrowtail=dot, dir=both, label=" groups (user)"];
django_contrib_auth_models_User -> django_contrib_auth_models_Permission  [arrowhead=dot, arrowtail=dot, dir=both, label=" user_permissions (user)"];
django_contrib_auth_models_User -> django_contrib_auth_models_AbstractUser  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
django_contrib_sessions_models_Session -> django_contrib_sessions_base_session_AbstractBaseSession  [arrowhead=empty, arrowtail=none, dir=both, label=" abstract\ninheritance"];
chat_models_Room -> django_contrib_auth_models_User  [arrowhead=dot, arrowtail=dot, dir=both, label=" users (rooms_joined)"];
store_models_PerfilVentas -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=none, dir=both, label=" user (perfilventas)"];
store_models_Producto -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (publicaciones)"];
store_models_Producto -> categoria_models_Categoria  [arrowhead=none, arrowtail=dot, dir=both, label=" categoria (producto)"];
comentarios_models_Comentarios -> social_models_Post  [arrowhead=none, arrowtail=dot, dir=both, label=" post (post_comentarios)"];
comentarios_models_Comentarios -> django_contrib_auth_models_User  [arrowhead=none, arrowtail=dot, dir=both, label=" user (user_comentarios)"];
tarjetas_models_CartItem -> store_models_Producto  [arrowhead=none, arrowtail=dot, dir=both, label=" producto (cartitem)"];
tarjetas_models_CartItem -> tarjetas_models_Cart  [arrowhead=none, arrowtail=dot, dir=both, label=" cart (cartitem)"];
"\n\n\n";
}

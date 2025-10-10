from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, Date, Text, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import os

# Caminho para o arquivo da base de dados SQLite
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'estudio_elsa_pilates.db')
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Criar engine e sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos de Dados
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), nullable=False)  # 'admin', 'instructor', 'student'
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20))
    first_name = Column(String(80))
    last_name = Column(String(80))
    
    def __repr__(self):
        return f'<User {self.username}>'

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    birth_date = Column(Date)
    anamnesis = Column(Text)
    is_active = Column(Boolean, default=True)
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    plan = Column(String(50))
    credits = Column(Integer, default=0)
    
    user = relationship("User", backref="student_profile")
    
    def __repr__(self):
        return f'<Student {self.id}>'

class Instructor(Base):
    __tablename__ = 'instructors'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    specialty = Column(String(100))
    hire_date = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", backref="instructor_profile")
    
    def __repr__(self):
        return f'<Instructor {self.id}>'

class Class(Base):
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    schedule_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, default=60)
    max_capacity = Column(Integer, default=10)
    instructor_id = Column(Integer, ForeignKey('instructors.id'), nullable=False)
    
    instructor = relationship("Instructor", backref="classes")
    
    def __repr__(self):
        return f'<Class {self.name}>'

class ClassAttendance(Base):
    __tablename__ = 'class_attendances'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    attended = Column(Boolean, default=False)
    attendance_date = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (UniqueConstraint('student_id', 'class_id', name='_student_class_uc'),)
    
    student = relationship("Student", backref="attendances")
    class_ = relationship("Class", backref="attendances")
    
    def __repr__(self):
        return f'<Attendance Student:{self.student_id} Class:{self.class_id}>'

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    category = Column(String(50))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    sold = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_method = Column(String(50))
    status = Column(String(20), default='completed')  # 'pending', 'completed', 'failed'
    payment_type = Column(String(20), nullable=False)  # 'plan', 'product'
    description = Column(String(255))
    
    student = relationship("Student", backref="payments")
    
    def __repr__(self):
        return f'<Payment {self.amount}>'

# Função para inicializar a base de dados
def init_db():
    Base.metadata.create_all(bind=engine)

# Função para obter uma sessão
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        pass

# Função para popular a base de dados com dados de exemplo
def populate_sample_data():
    db = SessionLocal()
    
    # Verificar se já existem dados
    if db.query(User).count() > 0:
        db.close()
        return
    
    # Criar utilizadores de teste
    admin_user = User(
        username="admin",
        password_hash="password",  # Em produção, usar hash real
        role="admin",
        email="admin@estudioelsa.com",
        phone="+351 912 345 678",
        first_name="Administrador",
        last_name="Sistema"
    )
    
    instructor_user = User(
        username="instructor",
        password_hash="password",
        role="instructor",
        email="instructor@estudioelsa.com",
        phone="+351 912 345 679",
        first_name="Maria",
        last_name="Silva"
    )
    
    student_user = User(
        username="student",
        password_hash="password",
        role="student",
        email="student@estudioelsa.com",
        phone="+351 912 345 680",
        first_name="João",
        last_name="Santos"
    )
    
    db.add_all([admin_user, instructor_user, student_user])
    db.commit()
    
    # Criar perfil de instrutor
    instructor = Instructor(
        user_id=instructor_user.id,
        specialty="Pilates Clássico"
    )
    db.add(instructor)
    db.commit()
    
    # Criar perfil de aluno
    student = Student(
        user_id=student_user.id,
        plan="Premium",
        credits=8,
        is_active=True
    )
    db.add(student)
    db.commit()
    
    # Criar produtos de exemplo
    products = [
        Product(name="Meias Antiderrapantes", category="Acessórios", price=8.50, stock=25, sold=15),
        Product(name="T-shirt Estúdio Elsa", category="Vestuário", price=22.00, stock=18, sold=8),
        Product(name="Garrafa de Água", category="Acessórios", price=12.00, stock=30, sold=20),
        Product(name="Leggings Premium", category="Vestuário", price=45.00, stock=12, sold=5),
        Product(name="Tapete de Yoga", category="Equipamento", price=35.00, stock=8, sold=3),
    ]
    db.add_all(products)
    db.commit()
    
    # Criar pagamentos de exemplo
    payments = [
        Payment(student_id=student.id, amount=80.00, payment_method="MB Way", status="completed", payment_type="plan", description="Mensalidade Premium - Janeiro"),
        Payment(student_id=student.id, amount=8.50, payment_method="Cartão", status="completed", payment_type="product", description="Meias Antiderrapantes"),
    ]
    db.add_all(payments)
    db.commit()
    
    db.close()

